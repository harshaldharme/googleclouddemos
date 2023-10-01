resource "google_compute_network" "terraform_network" {
  name = "terraform-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "terraform_subnet" {
    name = "tf-us-central1-c-subnet"
    ip_cidr_range = "10.20.0.0/16"
    region = "us-central1"
    network = google_compute_network.terraform_network.id
}