import streamlit as st
import requests
import plotly.graph_objects as go

# Professional Page Setup
st.set_page_config(page_title="FinOps Janitor Pro", page_icon="📈", layout="wide")

st.title("🛡️ FinOps Janitor: Executive Overview")
st.write("Programmatic Resource Governance & Fiscal Oversight")
st.divider()

# KPIs (Static for now, dynamic after audit)
col1, col2, col3 = st.columns(3)
col1.metric("Infrastructure Health", "Optimal", "GCP Active")
col2.metric("Detected Leakage", "₹105.00", "Monthly")
col3.metric("Project Scope", "3 Instances", "us-central1")

if st.button('🚀 EXECUTE CLOUD AUDIT'):
    with st.spinner('Pinging GCP Serverless Function...'):
        try:
            # 🔗 YOUR RECENTLY VERIFIED GCP URL
            url = "https://us-central1-finops-janitor-lab.cloudfunctions.net/finops-janitor-function"
            
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                st.success("Audit Successful")
                data = response.json()
                st.table(data['audit_results'])
            else:
                st.error(f"GCP Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Handshake Failed: {e}")

# Visuals
fig = go.Figure(data=[go.Pie(labels=['Waste', 'Operating'], values=[105, 450], hole=.6)])
st.plotly_chart(fig, width='stretch')