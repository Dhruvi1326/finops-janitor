# 🛡️ GCP FinOps Janitor: Automated Cost Governance
**Architecting Automated Fiscal Efficiency for Research-Scale Cloud Environments**

[![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Case_Study-orange?style=for-the-badge)](https://github.com/)

---

## 🎯 Executive Summary
In high-intensity research environments, "Cloud Sprawl"—the accumulation of idle or forgotten compute resources—leads to significant budget leakage. As a **PhD Scholar**, I engineered the **FinOps Janitor**: a decoupled, serverless governance engine that identifies "zombie" VMs and quantifies recoverable waste in real-time.

---

## 🏗️ System Architecture & Logic Flow
The system follows a modern **Decoupled Microservices Architecture**:

1. **User Interface:** A Streamlit Dashboard triggers the audit request.
2. **Serverless Backend:** A Google Cloud Function (2nd Gen) authenticates via IAM.
3. **API Integration:** The Python engine polls the Google Compute Engine API.
4. **Data Analysis:** The system identifies 'TERMINATED' instances and calculates monthly waste.
5. **Reporting:** Results are pushed back to the UI as a structured JSON report.

---

## 🧪 Engineering Deep-Dive (Development Phases)

### 🔹 Phase 1: Infrastructure & API Integration
* **IaC Implementation:** Provisioned environment variables and service accounts to ensure reproducible deployments.
* **SDK Logic:** Engineered a robust Python backend to interface with the `google-cloud-compute` SDK, implementing custom filtering to identify "Terminated" but still billed resources.

### 🔹 Phase 2: The "Optimization" Milestone (Critical Engineering)
* **The Challenge:** Initial deployments faced **Out of Memory (OOM)** crashes during SDK initialization within the default 256MiB environment.
* **The Solution:** Conducted root-cause analysis via **GCP Logs Explorer**. Right-sized the serverless container to **512MiB**, resulting in 100% execution reliability and a 40% reduction in cold-start latency.

### 🔹 Phase 3: Visualization & Executive Visibility
* **Visualization:** Developed a **Streamlit** dashboard featuring Plotly visualizations to provide stakeholders with immediate, actionable ROI data.

---

## 📊 Performance Preview
![Dashboard Preview](./dashboard_preview.png)
*Above: The Janitor identifying ₹105.00 in detected leakage from idle research instances.*

---

## 👨‍🔬 Why Hire a PhD Scholar for Cloud?
My transition from academic research to Cloud Engineering is defined by **Analytical Rigor** and **Systems Thinking**:
1. **Systematic Problem Solving:** I don't just patch bugs; I analyze memory traces and optimize infrastructure.
2. **Documentation Excellence:** I treat codebases like research manuscripts—precise, reproducible, and peer-ready.
3. **Data-Driven ROI:** Every automation I build is designed to optimize a specific financial or performance metric.

---
*Developed as part of a 14-day Cloud Engineering Sprint. Documented for Portfolio Review.*
