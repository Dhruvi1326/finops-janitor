# FinOps Janitor: Automated GCP Cost Optimization

> **Cloud-native Python automation to enforce fiscal governance by programmatically managing idle Compute Engine resources.**

---

### 🏛️ Phase 1: Architecture & Governance (Completed)
- **Infrastructure:** Provisioned via **Terraform (IaC)** for environment parity.
- **Logic Engine:** Python-based scanner using **Google Cloud SDK** for real-time resource auditing.
- **Policy Enforcement:** Implements **Metadata-based Exemptions** to protect critical workloads.
- **Safety Layer:** Global **Dry-Run** functionality to prevent unauthorized state changes.

## 📈 Phase 2: Dynamic Resource Fetching (Completed)
The Janitor is fully integrated with the **Google Cloud Compute Engine API** to audit real-time resource states.
- **Project Scope**: `finops-janitor-lab`
- **Discovery**: Successfully audits `research-vm-01`, `02`, and `03`.

## 🧠 Phase 3: Financial Intelligence & Waste Detection (Completed)
The system calculates the **Total Cost of Idle Resources**, focusing on persistent disk leakage in stopped instances.
- **Status Check**: Identifies `TERMINATED` instances that still incur storage costs.
- **Actionable ROI**: Generates reports showing potential monthly savings in INR (₹).

## ☁️ Phase 4: Serverless Deployment (Completed)
Transitioned from local script execution to a **Serverless Architecture** using **Google Cloud Functions (2nd Gen)**.
- **Deployment**: Automated via `gcloud` CLI with a Python 3.11 runtime.
- **Trigger**: HTTP-activated audit reports accessible via secure endpoint.
- **Efficiency**: Zero-cost idle state; resources are only consumed during the 5-second audit execution.

---
*This project demonstrates a full-cycle FinOps automation workflow: from IaC (Terraform) to Real-time Monitoring and Autonomous Lifecycle Management.*

### 🚀 Key Capabilities
- **Automated Discovery:** Identifies idle VMs based on customized resource tagging.
- **Governance Guardrails:** Recognizes `keep_alive` labels to bypass automated shutdowns.
- **Cloud-Native Scalability:** Deployed as a stateless function for 24/7 availability.

### 🛠️ Tech Stack
- **Cloud:** Google Cloud Platform (GCP)
- **Serverless:** Google Cloud Functions / Cloud Run
- **Automation:** Python 3.x (`google-cloud-compute`, `functions-framework`)
- **Infrastructure:** Terraform / HCL
