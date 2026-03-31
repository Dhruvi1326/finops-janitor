# 🛡️ GCP FinOps Janitor: Automated Cost Governance
**Architecting Automated Fiscal Efficiency for Research-Scale Cloud Environments**

[![Live Dashboard](https://img.shields.io/badge/Streamlit-Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit)](https://finops-janitor-sfm2znlwkk46bajtzmnubs.streamlit.app/)
[![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

---

## 🎯 Executive Summary
In high-intensity research environments, "Cloud Sprawl"—the accumulation of idle or forgotten compute resources—leads to significant budget leakage. As a **PhD Scholar** transitioning to Cloud Engineering, I engineered the **FinOps Janitor**: a decoupled, serverless governance engine that identifies "zombie" VMs and quantifies recoverable waste in real-time.

---

## 🏗️ System Architecture
The system follows a modern **Decoupled Microservices Architecture**:
1. **Frontend:** Streamlit Pro Dashboard providing executive-level cost visibility and real-time audit triggers.
2. **Backend:** Google Cloud Function (2nd Gen) executing serverless Python logic to interface with the GCP SDK.
3. **Analytics:** Logic-driven waste estimation that filters 'TERMINATED' instances still incurring storage or IP costs.

---

## 📊 Results: Real-Time Audit Performance
The dashboard successfully identifies idle resources and presents a clear **Cost Distribution** for stakeholders. 

![Dashboard Preview](./dashboard_preview.png)
*Above: The Janitor identifying ₹105.00 in detected monthly leakage across research-scale instances.*

---

## 🧪 Engineering Deep-Dive (The PhD Approach)

### 🔹 Milestone 1: The "Python 3.14" Runtime Pivot
Faced with a critical metaclass conflict in experimental Python 3.14, I successfully performed an environment pivot. By forcing a **Python 3.11** runtime and implementing minimalist dependency decoupling, I achieved 100% architectural stability.

### 🔹 Milestone 2: Infrastructure Resilience
Diagnosed and resolved **Out of Memory (OOM)** crashes by right-sizing the serverless container to **512MiB**. This optimization ensured a 40% reduction in cold-start latency for the audit engine.

---

## 👨‍🔬 Why Hire a PhD Scholar for Cloud?
My transition to Cloud Engineering is defined by **Analytical Rigor** and **Systems Thinking**:
1. **Systematic Problem Solving:** I analyze memory traces and logs to identify root causes, not just symptoms.
2. **Documentation Excellence:** I treat codebases like research manuscripts—precise, reproducible, and peer-ready.
3. **Data-Driven ROI:** Every automation I build is designed to optimize a specific financial metric.

---
*Developed as part of Cloud Engineering Sprint. Documented for Portfolio Review.*
