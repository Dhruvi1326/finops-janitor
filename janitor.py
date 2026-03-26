import os
import logging
from google.cloud import compute_v1
from google.api_core import exceptions

# 1. SETUP LOGGING (The Paper Trail)
# This creates a file called 'janitor.log' to record everything
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("janitor.log"),
        logging.StreamHandler()
    ]
)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

# 2. CONFIGURATION (The Safety Switches)
DRY_RUN = False  # Set to False to actually stop VMs
PROJECT_ID = "finops-janitor-lab"
ZONE = "us-central1-a"

def run_robust_janitor():
    try:
        client = compute_v1.InstancesClient()
        logging.info(f"🚀 Starting Audit. Mode: {'DRY RUN' if DRY_RUN else 'LIVE'}")
        
        instances = client.list(project=PROJECT_ID, zone=ZONE)

        for instance in instances:
            name = instance.name
            labels = instance.labels
            status = instance.status

            # Pillar 1: EXEMPTION LOGIC (Safety Sticker)
            if labels.get("keep_alive") == "true":
                logging.info(f"🛡️  SKIPPING: {name} is PROTECTED by label.")
                continue

            # Pillar 2: ACTION LOGIC (The Janitor's Decision)
            if status == "RUNNING" and labels.get("activity") == "idle":
                # Pillar 3: DRY RUN PROTECTION
                if DRY_RUN:
                    logging.warning(f"  [DRY RUN]: {name} is IDLE and would be stopped.")
                else:
                    logging.info(f" LIVE ACTION: Stopping {name}...")
                    client.stop(project=PROJECT_ID, zone=ZONE, instance=name)
            else:
                logging.info(f" NO ACTION: {name} is {status}.")

    # Pillar 4: ERROR HANDLING (The Safety Net)
    except exceptions.GoogleAPICallError as e:
        logging.error(f" Google Cloud API Error: {e}")
    except Exception as e:
        logging.error(f" Unexpected Error: {e}")

if __name__ == "__main__":
    run_robust_janitor()