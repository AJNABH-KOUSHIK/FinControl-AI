from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # use your existing db instance

# --- AUDIT TRAIL (Immutable Controller Log) ---
class ControllerAuditLog(db.Model):
    __tablename__ = 'controller_audit_log'
    id            = db.Column(db.Integer, primary_key=True)
    timestamp     = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    user_id       = db.Column(db.String(100), nullable=False, default='system')
    user_role     = db.Column(db.String(50), default='controller')
    action_type   = db.Column(db.String(50), nullable=False)  # approve, reject, view, ai_apply, escalate
    entity_type   = db.Column(db.String(50), nullable=False)  # recommendation, exception, variance, cashflow, ap_ar
    entity_id     = db.Column(db.String(100))
    description   = db.Column(db.Text, nullable=False)
    details_json  = db.Column(db.Text)  # full JSON context
    ai_context    = db.Column(db.Text)  # what the AI said/recommended
    approved_by   = db.Column(db.String(100))
    session_id    = db.Column(db.String(100))
    ip_address    = db.Column(db.String(45))

    def to_dict(self):
        return {
            "id": self.id, "timestamp": self.timestamp.isoformat(),
            "user": self.user_id, "action": self.action_type,
            "entity": f"{self.entity_type}:{self.entity_id}",
            "description": self.description, "ai_context": self.ai_context
        }

# --- EXCEPTION & CONTROL MONITORING ---
class ControllerException(db.Model):
    __tablename__ = 'controller_exceptions'
    id           = db.Column(db.Integer, primary_key=True)
    scan_id      = db.Column(db.String(80), index=True)
    exception_type = db.Column(db.String(60))  # duplicate_payment, missing_document, variance_alert, risk_flag, cash_anomaly
    severity     = db.Column(db.String(20), default='medium')  # low, medium, high, critical
    status       = db.Column(db.String(20), default='open')    # open, reviewing, resolved, rejected, escalated
    title        = db.Column(db.String(200))
    description  = db.Column(db.Text)
    amount_impact = db.Column(db.Float, default=0.0)
    assigned_to  = db.Column(db.String(100))
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at  = db.Column(db.DateTime, nullable=True)
    resolution_notes = db.Column(db.Text)

    @staticmethod
    def open_by_severity():
        return ControllerException.query.filter(
            ControllerException.status.in_(['open', 'escalated', 'reviewing'])
        ).order_by(db.desc(ControllerException.severity == 'critical')).all()

# --- APPROVAL & HUMAN-IN-THE-LOOP ---
class ControllerApproval(db.Model):
    __tablename__ = 'controller_approvals'
    id            = db.Column(db.Integer, primary_key=True)
    request_type  = db.Column(db.String(60))  # variance_override, exception_resolve, ai_recommendation, cash_transfer
    request_id    = db.Column(db.String(100), index=True)
    status        = db.Column(db.String(20), default='pending')  # pending, approved, rejected, escalated
    requested_by  = db.Column(db.String(100))
    assigned_to   = db.Column(db.String(100), default='finance_controller')
    ai_recommendation = db.Column(db.Text)  # raw AI text
    ai_confidence = db.Column(db.Float, default=0.0)  # 0-1
    decision      = db.Column(db.Text)
    comments      = db.Column(db.Text)
    amount        = db.Column(db.Float)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)
    decided_at    = db.Column(db.DateTime, nullable=True)

    @staticmethod
    def pending_for(user='finance_controller'):
        return ControllerApproval.query.filter_by(
            assigned_to=user, status='pending'
        ).order_by(ControllerApproval.created_at.asc()).all()

# --- CASH FLOW / FINANCIAL HEALTH ---
class CashFlowSnapshot(db.Model):
    __tablename__ = 'cashflow_snapshots'
    id              = db.Column(db.Integer, primary_key=True)
    snapshot_date   = db.Column(db.Date, default=lambda: datetime.utcnow().date())
    actual_cash     = db.Column(db.Float, default=0.0)
    projected_7d    = db.Column(db.Float, default=0.0)
    projected_30d   = db.Column(db.Float, default=0.0)
    health_score    = db.Column(db.Float, default=100.0)  # 0-100
    liquidity_ratio = db.Column(db.Float, default=0.0)
    risk_flags      = db.Column(db.String(200))  # comma-separated
    notes           = db.Column(db.Text)

# --- BUDGET VS ACTUAL / VARIANCE ---
class BudgetVariance(db.Model):
    __tablename__ = 'budget_variance'
    id            = db.Column(db.Integer, primary_key=True)
    period        = db.Column(db.String(20))  # Q3-2025, Oct-2025
    category      = db.Column(db.String(100))
    budget_amount = db.Column(db.Float, default=0.0)
    actual_amount = db.Column(db.Float, default=0.0)
    variance_pct  = db.Column(db.Float, default=0.0)  # can be negative
    status        = db.Column(db.String(20), default='ok')  # ok, warning, critical
    explanation   = db.Column(db.Text)
    requires_approval = db.Column(db.Boolean, default=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

# --- PAYABLES / RECEIVABLES ---
class APARItem(db.Model):
    __tablename__ = 'ap_ar_items'
    id          = db.Column(db.Integer, primary_key=True)
    item_type   = db.Column(db.String(10))  # AP or AR
    vendor_customer = db.Column(db.String(200))
    invoice_ref = db.Column(db.String(100))
    amount      = db.Column(db.Float, default=0.0)
    due_date    = db.Column(db.Date)
    status      = db.Column(db.String(20))  # pending, overdue, paid, disputed
    aging_days  = db.Column(db.Integer, default=0)
    risk_score  = db.Column(db.Float, default=0.0)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)