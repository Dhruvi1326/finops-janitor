# FinOps Janitor: Automated GCP Cost Optimization

> **Cloud-native Python automation to enforce fiscal governance by programmatically managing idle Compute Engine resources.**

---

### 🏛️ Phase 1: Architecture & Governance

- **Infrastructure:** Provisioned via **Terraform (IaC)** for environment parity.
- **Logic Engine:** Python-based scanner using **Google Cloud SDK** for real-time resource auditing.
- **Policy Enforcement:** Implements **Metadata-based Exemptions** to protect critical workloads.
- **Safety Layer:** Global **Dry-Run** functionality to prevent unauthorized state changes.

## 📈 Phase 2: Dynamic Resource Fetching (Completed)
The Janitor has moved beyond static mock data and is now fully integrated with the **Google Cloud Compute Engine API**.

### 🩺 Live Inventory Validation
The script now establishes a secure handshake with the GCP Control Plane to audit real-time resource states:
- **Project Scope**: `finops-janitor-lab`
- **Zone**: `us-central1-a`
- **Discovery**: Successfully retrieved and logged `research-vm-01`, `02`, and `03`.

## 🧠 Phase 3: Financial Intelligence & Waste Detection (Active)
The system is being upgraded to calculate the **Total Cost of Idle Resources**, focusing on unattached storage and persistent disk leakage.

### 🛡️ Financial Governance Logic
1. **Status Check**: Identify `TERMINATED` instances.
2. **Storage Audit**: Calculate the monthly "leak" from persistent boot disks.
3. **Actionable ROI**: Generate reports showing potential savings in INR (₹) to justify resource cleanup.

---
*This project demonstrates a full-cycle FinOps automation workflow: from IaC (Terraform) to Real-time Monitoring and Autonomous Lifecycle Management.*

### 🚀 Key Capabilities

- **Automated Discovery:** Identifies idle VMs based on customized resource tagging.
- **Governance Guardrails:** Recognizes `keep_alive` labels to bypass automated shutdowns.
- **Auditability:** Generates structured `janitor.log` files for FinOps compliance reporting.

### 🛠️ Tech Stack

- **Cloud:** Google Cloud Platform (GCP)
- **Automation:** Python 3.x (`google-cloud-compute`)
- **Infrastructure:** Terraform / HCL
- **Security:** Git-ignored service account authentication

---

### 🏃 Quick Start

1. `terraform apply` to provision the environment.
2. `python janitor.py` to execute the audit logic.
3. Review `janitor.log` for the action report.
4. `terraform destroy` (Optional) to tear down the lab and stop all costs.
