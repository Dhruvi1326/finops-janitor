# FinOps Janitor: Automated GCP Cost Optimization

> **Cloud-native Python automation to enforce fiscal governance by programmatically managing idle Compute Engine resources.**

---

### 🏛️ Phase 1: Architecture & Governance 
- **Infrastructure:** Provisioned via **Terraform (IaC)** for environment parity.
- **Logic Engine:** Python-based scanner using **Google Cloud SDK** for real-time resource auditing.

## 📈 Phase 2: Dynamic Resource Fetching 
The Janitor is fully integrated with the **Google Cloud Compute Engine API** to audit real-time resource states.

## 🧠 Phase 3: Financial Intelligence & Waste Detection 
The system calculates the **Total Cost of Idle Resources**, focusing on persistent disk leakage in stopped instances (Monthly Savings Estimate: ₹105.00).

## ☁️ Phase 4: Serverless Deployment 
Transitioned from local script execution to a **Serverless Architecture** using **Google Cloud Functions (2nd Gen)**.

## ⏰ Phase 5: Managed Orchestration 
Implemented **Autonomous Scheduling** to enforce governance without human intervention.
- **Orchestrator**: Google Cloud Scheduler.
- **Pattern**: Cron-based triggers (`0 2 * * *`) for daily 2:00 AM audits.
- **Validation**: Verified successful handshake between Scheduler and Serverless Function via GCP Logs.

---
*This project demonstrates a full-cycle FinOps automation workflow: from IaC (Terraform) to Real-time Monitoring and Autonomous Lifecycle Management.*

### 🛠️ Tech Stack
- **Cloud:** Google Cloud Platform (GCP)
- **Serverless:** Google Cloud Functions / Cloud Run
- **Scheduling:** Cloud Scheduler (Cron)
- **Automation:** Python 3.x (`google-cloud-compute`, `functions-framework`)
- **Infrastructure:** Terraform / HCL
