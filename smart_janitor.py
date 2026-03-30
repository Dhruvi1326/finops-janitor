import os
import time
from google.cloud import compute_v1
from google.cloud import monitoring_v3

# --- 1. CONFIGURATION ---

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
project_id = "finops-janitor-lab" 
zone = "us-central1-a"

# Initialize Clients
instance_client = compute_v1.InstancesClient()
metric_client = monitoring_v3.MetricServiceClient()

def get_cpu_usage(instance_name):
    """Queries the last 20 minutes of CPU data for a specific VM."""
    project_name = f"projects/{project_id}"
    now = time.time()
    
    # Define a 20-minute window
    interval = monitoring_v3.TimeInterval({
        "end_time": {"seconds": int(now)},
        "start_time": {"seconds": int(now - 1200)},
    })
    
    # Filter for CPU utilization of the specific instance
    results = metric_client.list_time_series(request={
        "name": project_name,
        "filter": f'metric.type = "compute.googleapis.com/instance/cpu/utilization" AND metric.labels.instance_name = "{instance_name}"',
        "interval": interval,
    })
    
    for result in results:
        if result.points:
            # CPU is a decimal (0.01 = 1%), so we multiply by 100
            return result.points[0].value.double_value * 100
    return 0.0

# --- 2. THE BRAIN (The Decision Loop) ---
print(f"--- 🤖 Smart Janitor Audit: {time.ctime()} ---")
print(f"DEBUG: Scanning zone {zone} for instances in project '{project_id}'...")

try:
    instances = instance_client.list(project=project_id, zone=zone)

    for instance in instances:
        name = instance.name
        labels = instance.labels
        status = instance.status
        
        print(f"\n🔎 Checking VM: {name}")

        # STEP A: Safety First (Metadata Override)
        if labels.get("keep_alive") == "true":
            print(f"  🛡️ RESULT: Protected by 'keep_alive' label. Skipping.")
            continue

        # STEP B: Status Check
        if status == "TERMINATED":
            print(f"  💤 RESULT: Already stopped. No action needed.")
            continue

        # STEP C: Real-Time Metric Check
        cpu = get_cpu_usage(name)
        
        # STEP D: The Logic Gate
        if labels.get("activity") == "idle":
            if cpu < 5.0:
                print(f"  🛑 RESULT: Truly Idle (CPU: {cpu:.2f}%). Action: SHUTTING DOWN...")
                # UNCOMMENT the line below to let the Janitor actually stop the VM
                # instance_client.stop(project=project_id, zone=zone, instance=name)
            elif cpu > 50.0:
                print(f"  ⚠️ RESULT: Labeled 'idle' but High CPU ({cpu:.2f}%). Possible ghost process. Skipping for safety.")
            else:
                print(f"  ✅ RESULT: Active but within normal range ({cpu:.2f}%).")
        else:
            print(f"  👤 RESULT: No 'idle' label found. Human is currently using this VM.")

except Exception as e:
    print(f"❌ Error during audit: {e}")

print("\n--- Audit Complete ---")