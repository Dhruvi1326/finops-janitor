# 🛡️ GCP FinOps Janitor: Automated Cost Governance
**Architecting Automated Fiscal Efficiency for Research-Scale Cloud Environments**

[![Live Dashboard](https://img.shields.io/badge/Streamlit-Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit)](https://finops-janitor-sfm2znlwkk46bajtzmnubs.streamlit.app/)
[![Stack](https://img.shields.io/badge/GCP_|_Python_|_Plotly-blue?style=for-the-badge)](#)

---

## 🎯 Executive Summary
In high-intensity research environments, "Cloud Sprawl"—the accumulation of idle compute resources—leads to budget leakage. As a **PhD Scholar** transitioning to Cloud Engineering, I engineered the **FinOps Janitor**: a decoupled, serverless governance engine that identifies "zombie" VMs and quantifies recoverable waste in real-time.

---

## 🏗️ System Architecture
1. **Frontend:** Streamlit Pro Dashboard providing executive-level cost visibility.
2. **Backend:** Google Cloud Function (2nd Gen) executing serverless Python logic.
3. **Connectivity:** Secure HTTPS Handshake between the frontend and the GCP SDK.

---

## 📊 Performance Preview
![Dashboard Preview](./dashboard_preview.png)
*Above: The Janitor identifying ₹105.00 in detected leakage from idle research instances.*

---

## 🧪 Engineering Deep-Dive
- **Runtime Pivot:** Resolved Python 3.14 compatibility issues by forcing a stable **Python 3.11** environment.
- **Resource Optimization:** Diagnosed OOM errors via **GCP Logs Explorer** and right-sized the container to **512MiB** for 100% reliability.

---
*Developed for Portfolio Review | 2026*
