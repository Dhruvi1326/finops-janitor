# 1. Define the Provider (The "Connector")
provider "google" {
  credentials = file("credentials.json")
  project     = "finops-janitor-lab"
  region      = "us-central1"
  zone        = "us-central1-a"
}

# 2. Define the Resources (The "Waste")
# We are creating 3 small VMs that are "idle"
resource "google_compute_instance" "idle_vms" {
  count        = 3
  name         = "research-vm-0${count.index + 1}"
  machine_type = "e2-micro" # Stays within Free Tier

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {} # Gives it a public IP
  }

  # THIS IS THE MOST IMPORTANT PART FOR FINOPS
  labels = {
    environment = "dev"
    activity    = "idle"
    owner       = "research-dept"
  }
}