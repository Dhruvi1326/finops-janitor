import functions_framework
from google.cloud import compute_v1
import json

@functions_framework.http
def finops_janitor_audit(request):
    """The Final Stable Auditor: Scans GCP and returns JSON data."""
    project_id = "finops-janitor-lab"
    zone = "us-central1-a"
    
    try:
        client = compute_v1.InstancesClient()
        instances = client.list(project=project_id, zone=zone)
        
        report = []
        for instance in instances:
            # FinOps Logic: Estimate waste for unused capacity
            waste = 105.00 if instance.status == "TERMINATED" else 0.00
            report.append({
                "name": instance.name,
                "status": instance.status,
                "machine_type": instance.machine_type.split('/')[-1],
                "waste_estimate_inr": waste
            })
        
        return json.dumps({"audit_results": report}), 200, {'Content-Type': 'application/json'}
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return json.dumps({"error": str(e)}), 500, {'Content-Type': 'application/json'}