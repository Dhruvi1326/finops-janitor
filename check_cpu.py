from google.cloud import monitoring_v3
import time
import os

# 1. Setup Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

client = monitoring_v3.MetricServiceClient()
project_id = "finops-janitor-lab" 
project_name = f"projects/{project_id}"

# 2. Define Time Window (Look at the last 20 minutes)
now = time.time()
seconds = int(now)
nanos = int((now - seconds) * 10**9)
interval = monitoring_v3.TimeInterval(
    {
        "end_time": {"seconds": seconds, "nanos": nanos},
        "start_time": {"seconds": (seconds - 1200), "nanos": nanos},
    }
)

# 3. Query CPU Utilization
results = client.list_time_series(
    request={
        "name": project_name,
        "filter": 'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
        "interval": interval,
        "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
    }
)

print("--- 🩺 VM CPU Health Check ---")
for result in results:
    vm_name = result.metric.labels['instance_name']
    # CPU is a decimal (0.01 = 1%), so we multiply by 100
    usage = result.points[0].value.double_value * 100
    print(f"VM: {vm_name} | Current CPU: {usage:.2f}%")


if not list(results):
    print("No CPU data found. Try starting your VMs and waiting 5 minutes!")