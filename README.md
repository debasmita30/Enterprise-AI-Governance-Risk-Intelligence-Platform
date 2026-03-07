<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Enterprise%20AI%20Governance&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Risk%20Intelligence%20Platform&descAlignY=58&descSize=18&descColor=7ecbff" width="100%"/>

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Production_Ready-22c55e?style=for-the-badge"/>
</p>

<p>
  <a href="https://enterprise-ai-governance-risk.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Click%20Here-2563eb?style=for-the-badge" alt="Live Demo"/>
  </a>
</p>

<br/>

> **A production-grade AI governance platform** that helps enterprises evaluate, select, deploy, and monitor AI technologies responsibly — with full audit trails, role-based workflows, and executive reporting.

<br/>

</div>

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🏗️ System Architecture](#-system-architecture)
- [📁 Project Structure](#-project-structure)
- [🔄 Workflow](#-workflow)
- [🛡️ Risk Scoring Model](#-risk-scoring-model)
- [🗄️ Database Schema](#-database-schema)
- [🚀 Getting Started](#-getting-started)
- [🐳 Docker Deployment](#-docker-deployment)
- [☁️ Cloud Deployment](#-cloud-deployment)
- [👤 Demo Credentials](#-demo-credentials)
- [📸 Screenshots](#-screenshots)
- [🗺️ Roadmap](#-roadmap)
- [👩‍💻 Author](#-author)

---

## 🎯 Overview

Enterprises adopting AI must navigate a complex landscape of competing priorities:

<table>
<tr>
<td align="center">🔒<br/><b>Security Risk</b></td>
<td align="center">📋<br/><b>Compliance</b></td>
<td align="center">🌍<br/><b>Data Residency</b></td>
<td align="center">🔗<br/><b>Vendor Lock-in</b></td>
<td align="center">💰<br/><b>Cost Efficiency</b></td>
<td align="center">⚡<br/><b>SLA Reliability</b></td>
</tr>
</table>

This platform provides a **structured, auditable, role-based governance framework** to support enterprise AI decision-making — simulating real-world internal deployment workflows across IT, Security, Procurement, and Engineering teams.

---

## ✨ Key Features

<details>
<summary><b>⚙️ Vendor Risk Evaluation Engine</b></summary>

- Multi-dimensional risk scoring across 6 axes
- Security, compliance, cost, SLA, and lock-in modeling
- **Monte Carlo cost simulation** (300 iterations)
- Automated risk categorization: `Low` / `Moderate` / `High`
- Radar visualization of full risk profile
- One-click executive PDF report generation

</details>

<details>
<summary><b>📊 Executive AI Dashboard</b></summary>

- Total vendors evaluated at a glance
- Average risk score across portfolio
- Safest vendor identification
- Evaluation history trend visualization
- ID-based traceable analytics

</details>

<details>
<summary><b>🏛️ Enterprise Governance Board</b></summary>

- Ranked vendor leaderboard with color-coded risk levels
- Filter by risk category and approval status
- Versioned evaluation history
- Audit-friendly, export-ready view

</details>

<details>
<summary><b>👥 Role-Based Workflow System</b></summary>

| Role | Permissions |
|------|-------------|
| **Admin** | Full access, approve/reject, manage users |
| **Analyst** | Submit evaluations (requires admin approval) |
| **Viewer** | Read-only access to reports and dashboards |

</details>

<details>
<summary><b>📝 Audit Logging</b></summary>

Every governance action is recorded with full traceability:
- ✅ Vendor creation
- ✅ Approval / rejection actions
- ✅ Soft delete & recovery
- ✅ User-action timestamping

</details>

<details>
<summary><b>📤 Export & Reporting</b></summary>

- Executive PDF risk reports
- Excel export of vendor rankings
- Structured deployment summaries

</details>

<details>
<summary><b>🔬 API Benchmark Simulation</b></summary>

Mirrors real AI deployment performance evaluation:
- Latency distribution analysis
- P95 measurement
- Throughput simulation
- SLA tier classification
- System health scoring

</details>

---

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph CLIENT["🌐 Client Layer"]
        UI[Streamlit SaaS UI]
    end

    subgraph AUTH["🔐 Auth & Role Layer"]
        RBAC[Role-Based Access Control]
        BCRYPT[bcrypt Password Hashing]
        SESSIONS[Session Management]
    end

    subgraph CORE["⚙️ Core Application"]
        direction LR
        EVAL[Vendor Risk\nEvaluation Engine]
        DASH[Executive\nDashboard]
        GOV[Governance\nBoard]
        BENCH[API Benchmark\nSimulator]
    end

    subgraph MODEL["📐 Risk Modeling Layer"]
        MONTE[Monte Carlo\nSimulation\n300 iterations]
        WEIGHT[Weighted Risk\nScoring Engine]
        SLA[SLA Tier\nModeling]
        COMP[Compliance\nRule Engine]
    end

    subgraph DATA["🗄️ Data Layer"]
        DB[(SQLite DB)]
        VENDORS[Vendors Table]
        AUDIT[Audit Log Table]
    end

    subgraph EXPORT["📤 Export Layer"]
        PDF[PDF Report\nGenerator]
        EXCEL[Excel Export]
    end

    UI --> AUTH
    AUTH --> CORE
    CORE --> MODEL
    MODEL --> DATA
    CORE --> EXPORT
    DATA --> VENDORS
    DATA --> AUDIT

    style CLIENT fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style AUTH fill:#1e1e3f,stroke:#8b5cf6,color:#fff
    style CORE fill:#1a3a2a,stroke:#22c55e,color:#fff
    style MODEL fill:#3a1a1a,stroke:#ef4444,color:#fff
    style DATA fill:#1a2a3a,stroke:#06b6d4,color:#fff
    style EXPORT fill:#2a1a3a,stroke:#a855f7,color:#fff
```

---

## 📁 Project Structure

```
enterprise-ai-governance/
│
├── 📄 app.py                        # Main Streamlit application entrypoint
├── 📄 requirements.txt              # Python dependencies
├── 🐳 Dockerfile                    # Container configuration
├── 📄 .dockerignore
├── 📄 README.md
│
├── 📂 modules/                      # Core application modules
│   ├── 📄 auth.py                   # Authentication & session management
│   ├── 📄 risk_engine.py            # Multi-factor risk scoring logic
│   ├── 📄 monte_carlo.py            # Cost simulation (300 iterations)
│   ├── 📄 compliance.py             # Rule-based compliance scoring
│   ├── 📄 sla_model.py              # SLA tier classification
│   └── 📄 benchmark.py             # API performance simulation
│
├── 📂 database/                     # Data persistence layer
│   ├── 📄 schema.py                 # Table definitions & migrations
│   ├── 📄 vendors.py                # Vendor CRUD operations
│   └── 📄 audit_log.py             # Governance action logging
│
├── 📂 pages/                        # Streamlit multi-page components
│   ├── 📄 1_dashboard.py            # Executive AI Dashboard
│   ├── 📄 2_evaluation.py           # Vendor Risk Evaluation
│   ├── 📄 3_governance.py           # Governance Board
│   ├── 📄 4_workflows.py            # Role-based approval workflows
│   └── 📄 5_benchmarks.py          # API Benchmark Simulation
│
├── 📂 reports/                      # Export & report generation
│   ├── 📄 pdf_generator.py          # Executive PDF reports
│   └── 📄 excel_export.py          # Excel vendor rankings
│
├── 📂 assets/                       # Static assets
│   └── 📄 styles.css               # Custom Streamlit styling
│
└── 📂 tests/                        # Unit & integration tests
    ├── 📄 test_risk_engine.py
    ├── 📄 test_auth.py
    └── 📄 test_database.py
```

---

## 🔄 Workflow

```mermaid
sequenceDiagram
    actor Analyst
    actor Admin
    participant System as 🖥️ Platform
    participant DB as 🗄️ Database
    participant Log as 📝 Audit Log

    Analyst->>System: Submit Vendor Evaluation
    System->>System: Run Risk Scoring Engine
    System->>System: Monte Carlo Simulation
    System->>DB: Save as PENDING
    System->>Log: Log: "Evaluation Submitted"
    System-->>Analyst: ✅ Submission Confirmed

    Admin->>System: Review Governance Board
    System->>DB: Fetch PENDING vendors
    DB-->>System: Return vendor list
    System-->>Admin: Display ranked leaderboard

    Admin->>System: Approve / Reject Vendor
    System->>DB: Update status → APPROVED
    System->>Log: Log: "Admin Approval Action"
    System-->>Admin: ✅ Workflow Complete

    Admin->>System: Generate PDF Report
    System-->>Admin: 📄 Executive Risk Report
```

---

## 🛡️ Risk Scoring Model

The platform evaluates vendors across **6 weighted dimensions**:

```
╔══════════════════════════════════════════════════════════╗
║              MULTI-FACTOR RISK SCORE FORMULA             ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Risk Score =                                            ║
║    (Security Score      × 0.30) +                        ║
║    (Compliance Score    × 0.25) +                        ║
║    (SLA Reliability     × 0.20) +                        ║
║    (Cost Efficiency     × 0.10) +                        ║
║    (Vendor Lock-in Risk × 0.10) +                        ║
║    (Data Residency      × 0.05)                          ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║  RISK CATEGORIES                                         ║
║  ● 0.00 – 0.39  →  🟢 Low Risk                          ║
║  ● 0.40 – 0.69  →  🟡 Moderate Risk                     ║
║  ● 0.70 – 1.00  →  🔴 High Risk                         ║
╚══════════════════════════════════════════════════════════╝
```

**Monte Carlo Simulation** runs 300 cost scenarios, sampling variance across:
- License fee uncertainty
- Integration overhead
- Operational cost drift
- Hidden compliance costs

---

## 🗄️ Database Schema

```mermaid
erDiagram
    VENDORS {
        int id PK
        string vendor_name
        float security_score
        float compliance_score
        float sla_score
        float cost_score
        float lock_in_score
        float data_residency_score
        float final_risk_score
        string risk_category
        string status
        string created_by
        string approved_by
        bool is_deleted
        datetime created_at
    }

    AUDIT_LOGS {
        int id PK
        string username
        string action
        string vendor_name
        datetime timestamp
    }

    USERS {
        int id PK
        string username
        string password_hash
        string role
        datetime created_at
    }

    USERS ||--o{ VENDORS : "creates"
    USERS ||--o{ AUDIT_LOGS : "generates"
    VENDORS ||--o{ AUDIT_LOGS : "tracked_by"
```

---

## 🚀 Getting Started

### Option 1 — Local Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/enterprise-ai-governance.git
cd enterprise-ai-governance

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the platform
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🐳 Docker Deployment

```bash
# Build the image
docker build -t ai-governance-platform .

# Run the container
docker run -p 8501:8501 ai-governance-platform

# Access at
http://localhost:8501
```

> 💡 The container dynamically binds to the assigned cloud port for seamless cloud deployment.

---

## ☁️ Cloud Deployment

This platform is cloud-native and deploys to any container-compatible service:

| Platform | Status |
|----------|--------|
| **Render** | ✅ Tested & Verified |
| **Railway** | ✅ Compatible |
| **AWS ECS** | ✅ Compatible |
| **Azure Container Apps** | ✅ Compatible |
| **Google Cloud Run** | ✅ Compatible |

---

## 👤 Demo Credentials

| Role | Username | Password | Access Level |
|------|----------|----------|--------------|
| 🔴 **Admin** | `admin` | `admin123` | Full platform access + approvals |
| 🟡 **Analyst** | `analyst` | `analyst123` | Submit evaluations (pending approval) |
| 🟢 **Viewer** | `viewer` | `viewer123` | Read-only reports & dashboards |

---

## 🗺️ Roadmap

```mermaid
gantt
    title Platform Roadmap
    dateFormat  YYYY-Q
    section Current
    Multi-factor Risk Scoring     :done, 2024-Q3, 1Q
    Monte Carlo Simulation        :done, 2024-Q3, 1Q
    Role-Based Workflows          :done, 2024-Q3, 1Q
    Docker + Cloud Deployment     :done, 2024-Q4, 1Q
    section Near-term
    Real-time API Benchmarking    :active, 2025-Q1, 1Q
    PostgreSQL Migration          :2025-Q1, 1Q
    Immutable Audit Ledger        :2025-Q2, 1Q
    section Future
    Multi-region Compliance Maps  :2025-Q3, 1Q
    Granular RBAC Controls        :2025-Q3, 1Q
    CI/CD Automation              :2025-Q4, 1Q
    Kubernetes Support            :2025-Q4, 1Q
```

---

## 💼 Enterprise Use Cases

| Use Case | Description |
|----------|-------------|
| 🔍 **AI Vendor Procurement** | Objective, multi-dimensional vendor comparison |
| 🏛️ **Internal AI Governance** | Structured deployment decision framework |
| 🔒 **Security Risk Assessment** | Quantified security posture per vendor |
| 🔄 **Cross-Functional Approvals** | IT, Security, Procurement workflow alignment |
| 📋 **Compliance Alignment** | Rule-based regulatory scoring |
| 📊 **Deployment Readiness** | SLA + benchmark-based go/no-go decision support |

---

## 🧑‍💻 Author

<div align="center">

<img src="https://github.com/identicons/debasmita.png" width="80" style="border-radius:50%"/>

### Debasmita Chatterjee

*Computer Science Undergraduate*

**Applied AI · Governance Systems · AI Deployment Strategy**

<p>
  <a href="https://linkedin.com/in/your-profile">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://github.com/your-username">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer" width="100%"/>

<p><sub>Built with ❤️ to demonstrate production-grade AI governance — not just experimental AI usage.</sub></p>

</div>
