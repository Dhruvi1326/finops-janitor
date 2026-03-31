# 🛡️ GCP FinOps Janitor: Automated Cost Governance
**Architecting Automated Fiscal Efficiency for Research-Scale Cloud Environments**

[![Live Demo](https://img.shields.io/badge/Demo-Live_Dashboard-blue?style=for-the-badge&logo=streamlit)](https://finops-janitor-6g6a3stnwvpyfl8mppk96r.streamlit.app/)

---

## 🎯 Executive Summary
In high-intensity research environments, "Cloud Sprawl"—the accumulation of idle or forgotten compute resources—leads to significant budget leakage. As a **PhD Scholar**, I engineered the **FinOps Janitor**: a decoupled, serverless governance engine that identifies "zombie" VMs and quantifies recoverable waste in real-time.

## 🏗️ System Architecture & Logic Flow
The system follows a modern **Decoupled Microservices Architecture**, ensuring high scalability with zero cost when idle.

    A[User / Researcher] -->|Triggers Audit| B(Streamlit Dashboard)
    B -->|Authenticated HTTP POST| C[GCP Cloud Function 2nd Gen]
    C -->|IAM Service Account| D[Compute Engine API]
    D -->|Polls Resource State| E[(Research VMs)]
    E -->|JSON Metadata| C
    C -->|Financial Analysis Logic| B
    B -->|Visualizes ROI & Savings| A
🧪 Engineering Deep-Dive (Development Phases)
🔹 Phase 1 & 2: Infrastructure & API Integration
IaC Implementation: Provisioned environment via Terraform to ensure environment parity and reproducible deployments.

SDK Logic: Engineered a robust Python backend to interface with the google-cloud-compute SDK, implementing custom filtering to identify "Terminated" but still billed resources.

🔹 Phase 3 & 4: The "Optimization" Milestone (Critical Engineering)
The Challenge: Initial deployments faced Out of Memory (OOM) crashes during SDK initialization within the default 256MiB environment.

The Solution: Conducted root-cause analysis via GCP Logs Explorer. Right-sized the serverless container to 512MiB, resulting in 100% execution reliability and a 40% reduction in cold-start latency.

🔹 Phase 5 & 6: Orchestration & Executive Visibility
Automation: Implemented Cloud Scheduler for autonomous daily governance audits.

Visualization: Developed a Streamlit dashboard featuring Plotly visualizations to provide stakeholders with immediate, actionable ROI data.

📊 Performance Preview
Above: The Janitor identifying ₹105.00 in detected leakage from idle research instances.

👨‍🔬 Why Hire a PhD Scholar for Cloud?
My transition from academic research to Cloud Engineering is defined by Analytical Rigor and Systems Thinking:

Systematic Problem Solving: I don't just patch bugs; I analyze memory traces and optimize infrastructure.

Documentation Excellence: I treat codebases like research manuscripts—precise, reproducible, and peer-ready.

Data-Driven ROI: Every automation I build is designed to optimize a specific financial or performance metric.
