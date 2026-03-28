# FinOps Janitor: Automated GCP Cost Optimization

> **Cloud-native Python automation to enforce fiscal governance by programmatically managing idle Compute Engine resources.**

---

### 🏛️ Architecture & Governance

- **Infrastructure:** Provisioned via **Terraform (IaC)** for environment parity.
- **Logic Engine:** Python-based scanner using **Google Cloud SDK** for real-time resource auditing.
- **Policy Enforcement:** Implements **Metadata-based Exemptions** to protect critical workloads.
- **Safety Layer:** Global **Dry-Run** functionality to prevent unauthorized state changes.

## 📈 Phase 2: Metric-Driven Intelligence (New)
To move beyond manual metadata, the Janitor now integrates with **Google Cloud Monitoring** to analyze live telemetry. This allows for data-driven decisions based on actual resource utilization.

### 🩺 Live Telemetry Validation
During Phase 2 testing, the script successfully captured real-time CPU utilization metrics from the `asia-south1-c` lab environment:
- **research-vm-02**: 80.54% CPU (Observed during startup burst)
- **research-vm-03**: 72.36% CPU (Observed during startup burst)

### 🛠️ New Dependencies
- **Library**: `google-cloud-monitoring`
- **Metric Type**: `compute.googleapis.com/instance/cpu/utilization`

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
