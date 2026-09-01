import json
from datetime import datetime
from .models.controller_models import ControllerAuditLog, ControllerException, ControllerApproval
# Import your existing AI agent
try:
    from treasury_ai_agent import TreasuryAgent  # adjust import
except ImportError:
    TreasuryAgent = None

class FinanceControllerAI:
    def __init__(self, db_session):
        self.db = db_session
        self.agent = TreasuryAgent() if TreasuryAgent else None

    # --- 1. GENERATE AI RECOMMENDATIONS ---
    def generate_recommendations(self, scan_context: dict) -> list:
        """
        Returns structured recommendations for the controller.
        Example: "Approve 5% variance in Marketing — seasonal campaign expected."
        """
        recommendations = []

        # Pull open exceptions
        exceptions = ControllerException.query.filter_by(status='open').limit(10).all()
        for ex in exceptions:
            rec_text = self._build_exception_recommendation(ex)
            # Create approval request automatically for critical/high items
            if ex.severity in ('high', 'critical'):
                approval = ControllerApproval(
                    request_type='exception_resolve',
                    request_id=str(ex.id),
                    status='pending',
                    requested_by='ai_system',
                    assigned_to='finance_controller',
                    ai_recommendation=rec_text,
                    ai_confidence=0.88 if ex.severity == 'critical' else 0.72,
                    comments=f"Exception detected in scan: {ex.title}"
                )
                self.db.session.add(approval)
            
            recommendations.append({
                "id": f"rec_{ex.id}",
                "type": "exception_review",
                "title": ex.title,
                "description": ex.description,
                "severity": ex.severity,
                "ai_recommendation": rec_text,
                "confidence": 0.92,
                "action_required": ex.severity in ('high', 'critical'),
                "entity_id": ex.id
            })

        # Variance recommendations
        variances = BudgetVariance.query.filter_by(requires_approval=True).limit(5).all()
        for v in variances:
            rec_text = f"Review {v.category} variance of {v.variance_pct:.1f}%. {v.explanation or 'No explanation provided.'}"
            recommendations.append({
                "id": f"rec_var_{v.id}",
                "type": "variance_approval",
                "title": f"Budget Variance: {v.category}",
                "description": f"Period: {v.period} | Variance: {v.variance_pct:.1f}%",
                "severity": v.status,
                "ai_recommendation": rec_text,
                "confidence": 0.85,
                "action_required": True,
                "entity_id": v.id
            })

        return recommendations

    def _build_exception_recommendation(self, ex: ControllerException) -> str:
        # Hook into your LLM / AI agent
        if self.agent:
            prompt = f"""
            You are a Finance Controller AI. An exception was detected:
            Type: {ex.exception_type}
            Severity: {ex.severity}
            Description: {ex.description}
            Impact: ${ex.amount_impact}
            
            Recommend one specific action: Investigate, Approve Override, Escalate, or Resolve.
            Give a 1-sentence reason.
            """
            try:
                result = self.agent.run_query(prompt, context={"scan_id": ex.scan_id})
                return result.get('answer', 'Review required — insufficient context.')
            except Exception:
                pass
        # Fallback structured recommendation
        actions = {
            'duplicate_payment': 'Escalate to treasury — potential duplicate vendor payment detected.',
            'missing_document': 'Request documentation from vendor before approval.',
            'variance_alert': 'Approve only if seasonal/campaign-related; else investigate.',
            'cash_anomaly': 'Investigate cash position immediately — liquidity risk.'
        }
        return actions.get(ex.exception_type, 'Manual controller review required.')

    # --- 2. CASH HEALTH MONITORING ---
    def compute_cash_health(self, actual: float, projected_30d: float) -> dict:
        score = max(0, min(100, 100 - max(0, (actual - projected_30d) / max(actual, 1) * 100)))
        risk = []
        if actual < projected_30d * 0.8:
            risk.append("cash_shortfall_30d")
        if actual < 0:
            risk.append("negative_liquidity")
        return {
            "health_score": round(score, 1),
            "status": "healthy" if score > 75 else "warning" if score > 50 else "critical",
            "risk_flags": ",".join(risk) if risk else "none"
        }

    # --- 3. LOG EVERY CONTROLLER ACTION ---
    def log_action(self, user_id: str, action: str, entity_type: str, entity_id: str, 
                   description: str, ai_context: str = None, session_id: str = None, 
                   ip: str = "127.0.0.1"):
        log = ControllerAuditLog(
            user_id=user_id,
            action_type=action,
            entity_type=entity_type,
            entity_id=str(entity_id),
            description=description,
            ai_context=ai_context,
            session_id=session_id,
            ip_address=ip
        )
        self.db.session.add(log)
        self.db.session.commit()
        return log