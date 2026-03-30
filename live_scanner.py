from google.cloud import compute_v1

def audit_my_infrastructure(project_id):
    # Initialize the Compute Client
    instance_client = compute_v1.InstancesClient()
    zone = "us-central1-a"  # Where your Terraform VMs are
    
    print(f"🛰️ Accessing Project: {project_id}...")
    
    try:
        # Fetch the list of instances in your zone
        instances = instance_client.list(project=project_id, zone=zone)
        
        print("\n" + "="*40)
        print(f"{'VM NAME':<20} | {'STATUS':<15}")
        print("="*40)
        
        found_any = False
        for instance in instances:
            found_any = True
            status = instance.status
            name = instance.name
            
            # Simple Logic: If it's TERMINATED, it's potential waste (Disk costs)
            if status == "TERMINATED":
                status_display = f"❌ {status} (WASTE)"
            else:
                status_display = f"✅ {status}"
                
            print(f"{name:<20} | {status_display:<15}")
        
        if not found_any:
            print("📭 No VMs found. Check your project ID or Zone.")

    except Exception as e:
        print(f"❌ Connection Error: {e}")

MY_PROJECT = "finops-janitor-lab" 
audit_my_infrastructure(MY_PROJECT)