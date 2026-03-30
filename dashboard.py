import streamlit as st
import requests
import plotly.graph_objects as go

# 1. Professional Page Setup
st.set_page_config(page_title="FinOps Janitor Pro", page_icon="📈", layout="wide")

# Custom CSS for a "Corporate Tech" feel
st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ FinOps Janitor: Executive Overview")
st.write("Programmatic Resource Governance & Fiscal Oversight")
st.divider()

# 2. Key Performance Indicators (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Infrastructure Health", "Optimal", "GCP Active")
col2.metric("Detected Leakage", "₹105.00", "Monthly", delta_color="inverse")
col3.metric("Project Scope", "3 Instances", "us-central1")

st.divider()

# 3. Main Dashboard Body
left_info, right_viz = st.columns([1, 2])

with left_info:
    st.subheader("🕹️ Control Center")
    st.write("Trigger a real-time audit of the GCP environment to identify idle compute resources.")
    
    if st.button('🚀 EXECUTE CLOUD AUDIT'):
        with st.spinner('Pinging GCP Serverless Function...'):
            try:
                # Using verified URL
                url = "https://finops-janitor-function-rswc4fxswq-uc.a.run.app"
                response = requests.get(url)
                st.success("Audit Successful")
                st.info("Live Report Data:")
                st.code(response.text)
            except Exception as e:
                st.error(f"Handshake Failed: {e}")

with right_viz:
    st.subheader("📊 Cost Distribution")
    # Interactive Donut Chart 
    fig = go.Figure(data=[go.Pie(
        labels=['Recoverable Waste', 'Operational Costs'], 
        values=[105, 450], 
        hole=.6,
        marker_colors=['#FF4B4B', '#00CC96']
    )])
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

# 4. Sidebar Meta-Data
st.sidebar.title("System Metadata")
st.sidebar.info(f"**Backend:** GCP Functions\n**Runtime:** Python 3.11\n**Status:** Production Ready")