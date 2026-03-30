import functions_framework
from google.cloud import compute_v1

@functions_framework.http
def finops_janitor_audit(request):
    client = compute_v1.InstancesClient()
    project_id = "finops-janitor-lab"
    zone = "us-central1-a"
    COST_PER_GB_INR = 3.5 
    
    instances = client.list(project=project_id, zone=zone)
    total_waste = 0
    results = []

    for inst in instances:
        if inst.status == "TERMINATED":
            leak = 10 * COST_PER_GB_INR
            total_waste += leak
            results.append(f"❌ {inst.name}: Waste ₹{leak:.2f}")
        else:
            results.append(f"✅ {inst.name}: Active")
    
    summary = f"\n📈 TOTAL MONTHLY SAVINGS: ₹{total_waste:.2f}"
    full_report = "\n".join(results) + "\n" + "="*30 + summary
    
    return full_report, 200