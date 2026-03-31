import streamlit as st
import requests
import plotly.graph_objects as go

# 1. Professional Page Setup
st.set_page_config(page_title="FinOps Janitor Pro", page_icon="📈", layout="wide")

# Custom CSS for "Corporate Tech" UI
st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; background-color: #FF4B4B; color: white; }
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
    st.write("Trigger a real-time audit of the GCP environment.")
    
    if st.button('🚀 EXECUTE CLOUD AUDIT'):
        with st.spinner('Pinging GCP Serverless Function...'):
            try:
                # 🔗 Your verified GCP URL
                url = "https://us-central1-finops-janitor-lab.cloudfunctions.net/finops-janitor-function"
                response = requests.get(url, timeout=15)
                
                if response.status_code == 200:
                    st.success("Audit Successful")
                    try:
                        data = response.json()
                        if "audit_results" in data:
                            st.table(data['audit_results'])
                        else:
                            st.info("Raw Data Received:")
                            st.json(data)
                    except Exception:
                        st.warning("Audit complete, but response was not in JSON format.")
                        st.text(f"Raw Output: {response.text}")
                else:
                    st.error(f"GCP Access Error ({response.status_code})")
                    
            except Exception as e:
                # This only triggers if the URL is wrong or the internet is down
                st.error(f"Connection Failed: Check GCP Trigger URL")

with right_viz:
    st.subheader("📊 Cost Distribution")
    fig = go.Figure(data=[go.Pie(
        labels=['Recoverable Waste', 'Operational Costs'], 
        values=[105, 450], 
        hole=.6,
        marker_colors=['#FF4B4B', '#00CC96']
    )])
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), showlegend=True)
    st.plotly_chart(fig, width='stretch')

# 4. Sidebar Metadata
st.sidebar.title("System Metadata")
st.sidebar.info(f"**Backend:** GCP Functions\n**Runtime:** Python 3.11\n**Status:** Production Ready")