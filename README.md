# FinOps Janitor: Automated GCP Cost Optimization

> **Cloud-native Python automation to enforce fiscal governance by programmatically managing idle Compute Engine resources.**

---

### 🏛️ Architecture & Governance

- **Infrastructure:** Provisioned via **Terraform (IaC)** for environment parity.
- **Logic Engine:** Python-based scanner using **Google Cloud SDK** for real-time resource auditing.
- **Policy Enforcement:** Implements **Metadata-based Exemptions** to protect critical workloads.
- **Safety Layer:** Global **Dry-Run** functionality to prevent unauthorized state changes.

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
