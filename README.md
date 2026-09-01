<div align="center">

# 🏛️ FinControl AI

### *Reconciliation that explains itself.*

> An **autonomous AI Finance Controller** for SMEs — upload invoices and bank statements, and FinControl AI matches payments across currencies, hunts for fraud, explains every discrepancy in plain English, and hands you an audit-ready PDF report. No spreadsheets. No guesswork. No chasing.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-fincontrol--ai.onrender.com-brightgreen?style=for-the-badge)](https://fincontrol-ai.onrender.com/)
[![Task](https://img.shields.io/badge/Task_4-AI_Finance_Controller-blueviolet?style=for-the-badge)]()
[![Built For](https://img.shields.io/badge/Razorpay_AI_Builder-Internship_2026-0a66c2?style=for-the-badge&logo=razorpay&logoColor=white)]()
[![Runs Offline](https://img.shields.io/badge/Runs-With_or_Without_API_Key-brightgreen?style=for-the-badge)]()
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()
[![AI](https://img.shields.io/badge/AI-DeepSeek_V3.2-orange?style=for-the-badge)]()
[![Deployed On](https://img.shields.io/badge/Deployed_On-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)]()

<br/>

### 🔗 [**Watch the live product → fincontrol-ai.onrender.com**](https://fincontrol-ai.onrender.com/)

<br/>

</div>

---

## 🎯 Why "FinControl AI" — and why it *is* Task 4

Task 4 asked for an **AI Finance Controller**: something that doesn't just crunch numbers, but *behaves* like the person a finance team actually hires to sit across every ledger, question every anomaly, and sign off on the books.

A Finance Controller's job isn't to calculate — a spreadsheet already does that. A Controller's job is to:

- **Verify** that what was billed matches what was paid, across currencies and formats.
- **Challenge** anything that looks wrong — a duplicate, a phantom vendor, a missing reference.
- **Explain**, in writing, why every number is either fine or flagged.
- **Sign off** with a report an auditor can actually use.

That's precisely the shape of this product, which is why the name changed from a generic "Treasury AI" to **FinControl AI** — it isn't just moving treasury data around, it's exercising *control*: reconciliation, exception management, variance tracking, and human-in-the-loop approvals, all in one command view. The landing page literally frames it as "**Financial clarity, without the chase**" — the exact promise a Finance Controller makes to a CFO.

---

## 🧠 The Core Idea

Most "AI finance" demos let a language model touch the actual numbers — which means the numbers can hallucinate. FinControl AI refuses to do that.

> **Core principle:** reconciliation matching is **deterministic, auditable code**. The AI never decides a number — it only explains, reasons, and advises on numbers that a rules engine already computed.

This is the difference between an AI that *replaces* a Controller and an AI that *is* one: a real Controller doesn't invent the balance sheet either — they interrogate it. FinControl AI's language model layer is an **analyst, not a calculator**, which is exactly the trust boundary a finance function needs before it will let AI near real money.

---

## ⚙️ What Makes It Stand Out

| What most hackathon finance bots do | What FinControl AI does instead |
|---|---|
| One AI call does "everything," including the math | Matching engine is deterministic code; AI only explains and advises |
| Breaks completely without an API key | **Fully functional with zero API key** — deterministic fallback reasoning, clearly labeled "offline mode" |
| A single "upload and match" screen | A full **Controller Command Center**: cash flow, exceptions, variance, AP/AR, AI actions, approvals, and audit trail |
| Static match/no-match output | **Confidence-scored** matches (Matched / Partial / Suspicious / Unmatched) with an executive dashboard |
| No memory of past work | **Session-based Scan History** — every analysis is retained and revisitable |
| Fraud detection as an afterthought | Dedicated **Risk & Fraud** engine: duplicate payments, abnormal amounts, unknown vendors, missing references |
| A chatbot bolted on the side | **Scan-aware AI Copilot** that already knows the numbers in front of it — no re-explaining your own data to your own tool |
| A summary paragraph at the end | One-click **professional PDF audit report** — the actual deliverable a real Controller has to produce |

The screenshots tell the same story end-to-end: a landing page that sells the *outcome* ("Financial clarity, without the chase"), a guided 3-step workflow (Upload → Process → Results), a results dashboard with real reconciliation math (1/6 reconciled, 3 flagged suspicious, 40% average confidence on a genuinely messy dataset), and a **Finance Controller Command view** layering cash flow forecasting, a live exception queue with dollar-value impact, and pending human approvals on top of it.

---

## 🖥️ Product Walkthrough

**1. Landing — the pitch, in one screen**
A dark, boardroom-grade interface (not a generic Bootstrap template) makes the case in one sentence: FinControl AI turns scattered financial documents into reconciled, explainable, audit-ready intelligence, with a live "Reconciliation pulse" preview already running in the background.

**2. New Analysis — the workflow**
A 3-step guided flow (**Upload → Process → Results**) accepts an invoices file and a bank statement file (CSV, Excel, or digital PDF), with the expected columns spelled out so there's zero ambiguity about what the engine needs.

**3. Analysis Results — the verdict**
The Overview tab doesn't just say "done" — it shows exactly what the deterministic engine found: how many transactions cleared, how many need attention, how many were flagged suspicious, and the model's average confidence, backed by a reconciliation-status bar chart and a match-distribution donut.

**4. Finance Controller — the command center**
This is the tab that earns the "Controller" in the name: a live cash-health score, an open-exceptions counter, pending approvals awaiting a human, and an **Exception & Control Monitor** that ranks issues by severity and dollar impact (a $12,400 duplicate vendor payment flagged *critical*, not buried in a log file).

---

## 🚀 Feature Set

- **Smart Document Upload** — CSV, Excel, and digital PDF
- **AI Data Extraction** — invoice number, amount, currency, vendor, reference, date
- **Deterministic Reconciliation Engine** — Matched / Partial / Suspicious / Unmatched, with confidence scoring
- **AI Reasoning** — structured "Explain" modal for any transaction, powered by DeepSeek V3.2
- **AI Copilot** — a scan-aware chat assistant that already has your reconciliation context
- **Fraud & Risk Detection** — duplicates, abnormal amounts, unknown vendors, missing references
- **Finance Controller Dashboard** — cash flow & forecast, exception monitor, variance tracking, AP/AR, pending approvals, full audit trail
- **Executive Overview** — KPIs, charts, confidence scores, real-time alerts
- **Scan History** — every analysis retained for the session
- **One-Click Audit Report** — professional, exportable PDF

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python_3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-2A9D8F?style=flat-square&logo=gunicorn&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![DeepSeek](https://img.shields.io/badge/DeepSeek_V3.2-FF6B35?style=flat-square)
![Chutes AI](https://img.shields.io/badge/Chutes_AI-8A2BE2?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-217346?style=flat-square&logo=microsoft-excel&logoColor=white)
![PDFPlumber](https://img.shields.io/badge/pdfplumber-EC1C24?style=flat-square)
![ReportLab](https://img.shields.io/badge/ReportLab-B22222?style=flat-square)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

</div>

| Layer | What's used | Why it's the right call here |
|---|---|---|
| **Backend / API** | Python 3.11+, FastAPI, Uvicorn (ASGI) | Async, fast to iterate on during a hackathon timeline, and battle-tested for JSON-heavy financial APIs |
| **Frontend** | Single-file HTML / CSS / JavaScript — no React/Vue build step | Zero build tooling, zero framework overhead — loads instantly, and every reviewer can open one file and read the whole UI |
| **AI Reasoning Layer** | Chutes AI, model: `deepseek-ai/DeepSeek-V3.2-TEE`, with a **deterministic, data-grounded fallback** written in-house | Keeps the "analyst, not calculator" boundary — the LLM explains numbers a rules engine already froze, so a flaky or missing API key never breaks the demo |
| **Document Extraction** | `openpyxl` (Excel), `pdfplumber` (digital PDF), native CSV parsing | Covers the three formats real SME finance teams actually send — no forcing a single upload format |
| **Reconciliation Engine** | Hand-written deterministic matching logic (no AI in the numeric path) | Every match, mismatch, and confidence score is fully explainable and reproducible — auditable by design |
| **Reporting** | `reportlab` | Generates the one-click, print-ready PDF audit report — the actual artifact a real Controller has to hand over |
| **Data Handling** | Pandas-style tabular processing across CSV/Excel/PDF inputs | Normalizes messy, inconsistent finance exports into one clean schema before matching runs |
| **Deployment / Hosting** | **Render** (Python web service, `uvicorn` entrypoint) | One-command deploy straight from GitHub, free-tier friendly for a hackathon submission, and gives reviewers a live URL instead of asking them to `git clone` |
| **Version Control** | Git + GitHub | Full commit history for judges to trace how the project evolved |

> **Live, deployed build:** the exact same FastAPI app described above is running in production right now on Render — no local setup required to see it work end-to-end: **[fincontrol-ai.onrender.com](https://fincontrol-ai.onrender.com/)**

---

## ⚠️ Note for Reviewers

**The application runs fully without an API key.** Reconciliation, fraud detection, the dashboard, the PDF audit report, and scan history all work with no key required.

The **AI explanation** and **AI Copilot** features use a built-in **deterministic fallback** unless a Chutes AI key is supplied — they still return correct, data-grounded results (a small "offline mode" label appears on AI responses). This is by design, so the reviewer never hits a dead end.

To enable the **live AI** experience (Chutes AI / DeepSeek), set the `CHUTES_API_KEY` environment variable before running — the key is provided separately in the submission notes for security, and is intentionally not stored in this repo.

---

## 📦 Setup — do this once

**1. Install Python 3.11+** from [python.org](https://python.org). On Windows, tick **"Add Python to PATH"** during install.

```bash
python --version
```

**2. Get the project**

```bash
git clone https://github.com/Hashreena/treasury-ai.git
cd treasury-ai
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Running the app — every time

The app runs **with or without** an API key. To run with **live AI**, set the three environment variables and start the server **in the same terminal window**. To run **without** a key (offline fallback), skip the `CHUTES_...` lines and just run the final `uvicorn` command.

**Windows (PowerShell)**

```powershell
$env:CHUTES_API_KEY = "<provided in our submission notes>"
$env:CHUTES_API_URL = "https://llm.chutes.ai/v1/chat/completions"
$env:CHUTES_MODEL = "deepseek-ai/DeepSeek-V3.2-TEE"
python -m uvicorn app.main:app --reload
```

**Mac / Linux (Terminal)**

```bash
export CHUTES_API_KEY="<provided in our submission notes>"
export CHUTES_API_URL="https://llm.chutes.ai/v1/chat/completions"
export CHUTES_MODEL="deepseek-ai/DeepSeek-V3.2-TEE"
python -m uvicorn app.main:app --reload
```

Wait for `Application startup complete`, then open:

```
http://127.0.0.1:8000
```

Stop the server with `Ctrl + C`.

> **Important:** the environment variables and the server must be set in the **same terminal window**. If the AI features show "offline mode" while you expect live AI, the key was either not set, or set in a different window than the one running the server.

---

## 🧭 How to Use It

> 🚀 **Fastest path:** just open **[fincontrol-ai.onrender.com](https://fincontrol-ai.onrender.com/)** — it's live, deployed, and already runs the same build described in this README. Run it locally only if you want to test with your own `CHUTES_API_KEY`.

1. The landing page opens — click **Begin Analysis**
2. Upload an invoices file and a bank statement file (test files are in `datasets/`)
3. Watch it process, then explore: **Overview → Reconciliation → Risk & Fraud → Audit Report → Controller**
4. Click **Explain** on any transaction for AI reasoning
5. Ask the **Copilot** (bottom-right) questions about the scan
6. Download the **PDF audit report**
7. Revisit past runs anytime in **Scan History**

---

## 🧪 Test Datasets

7 ready-made reconciliation scenarios live in `datasets/`. Each folder contains a matching pair — `invoices.csv` and `bank_statement.csv` — upload the pair together into the FinControl AI workspace.

| Folder | Scenario | What it demonstrates |
|---|---|---|
| `01_clean_books` | Mostly matched, one minor FX variance | Calm baseline — a healthy books walkthrough |
| `02_fraud_alert` | Duplicate invoice + unknown merchant + missing reference | Core fraud-detection triggers, all in one scan |
| `03_fx_variances` | Every invoice partial — cross-border currency spread | How the engine handles multi-currency partial matches |
| `04_unpaid_invoices` | Several invoices with no matching payment | Unpaid/outstanding invoice tracking |
| `05_enterprise_batch` | Large 10-invoice batch, mixed outcomes | Scale — the "big demo" dataset |
| `06_small_business` | Small, simple, mostly clean | Quick, fast happy-path demo |
| `07_high_risk_audit` | Duplicates, abnormal amount, offshore wire | Heaviest risk profile — the strongest fraud showcase |

**How to run one:** open **New Analysis**, drop that folder's `invoices.csv` into the Invoices slot and its `bank_statement.csv` into the Bank Statement slot, then click **Start Analysis**. Keep pairs together — mixing files from different folders won't reproduce the intended scenario.

> **💡 Demo tip:** use **`02_fraud_alert`** or **`07_high_risk_audit`** to show off fraud detection at its sharpest. Use **`01_clean_books`** or **`06_small_business`** for a calm, confident "happy path" walkthrough.

---

## 🗂️ Project Structure

```
treasury-ai/
  app/
    main.py             FastAPI server & all endpoints
    reconciliation.py   deterministic matching engine
    fraud.py            fraud & risk detection
    reasoning.py        AI layer (explain + copilot)
    extraction.py       CSV / Excel / PDF parsing
    report.py           audit report builder
    report_pdf.py       PDF generator
    sample_data.py      built-in sample data
    landing.html        landing page
    dashboard.html      the workspace UI
  datasets/             7 test datasets
  requirements.txt      Python dependencies
  README.md             this file
```

---

## 🩹 Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Dependencies not installed — run `python -m pip install -r requirements.txt` |
| `python` is not recognized | Python isn't on PATH — reinstall and tick "Add Python to PATH" |
| AI features show "offline mode" | No API key set (the app still fully works — this is the deterministic fallback). Set all three `CHUTES_...` variables in the **same terminal** that runs the server |
| Page won't load | Confirm the terminal shows `Application startup complete`, then visit `http://127.0.0.1:8000` |

---

## 🗺️ Notes & Roadmap

- Scan history is **session-based** — it resets on server restart. **Persistent storage and user accounts** are the next milestone.
- Document extraction currently supports CSV, Excel, and **digital** PDFs. **OCR for scanned receipts** is on the roadmap.
- Planned: multi-user role-based approvals, bank-feed API integrations, and richer anomaly-detection models beyond rule-based fraud checks.

---

<div align="center">

### Built for the **Razorpay AI Builder Internship 2026** — Task 4: AI Finance Controller

*FinControl AI doesn't just process transactions. It controls them.*

</div>
