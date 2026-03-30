from google.cloud import compute_v1

def run_financial_audit(project_id):
    client = compute_v1.InstancesClient()
    zone = "us-central1-a"
    
    # 2026 Estimated Pricing for Standard Persistent Disk (per GB/month)
    COST_PER_GB_INR = 3.5 

    print(f"💰 Starting Financial Audit for: {project_id}")
    instances = client.list(project=project_id, zone=zone)
    
    total_monthly_waste = 0

    print("\n" + "="*55)
    print(f"{'VM NAME':<18} | {'STATUS':<12} | {'MONTHLY LEAK (₹)'}")
    print("="*55)

    for inst in instances:
        # Most of research-vms likely use a 10GB default boot disk
        disk_size = 10 
        
        if inst.status == "TERMINATED":
            leak = disk_size * COST_PER_GB_INR
            total_monthly_waste += leak
            status_display = f"❌ {inst.status}"
            cost_display = f"₹{leak:.2f}"
        else:
            status_display = f"✅ {inst.status}"
            cost_display = "₹0.00 (Active)"
            
        print(f"{inst.name:<18} | {status_display:<12} | {cost_display}")

    print("="*55)
    print(f"📈 TOTAL ESTIMATED MONTHLY SAVINGS: ₹{total_monthly_waste:.2f}")
    print("="*55)

run_financial_audit("finops-janitor-lab")