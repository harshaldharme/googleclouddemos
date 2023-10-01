provider "google" {
    project = "cloudstudy-131288"
    credentials = "${file("credentials.json")}"
    region = "us-central1"
    zone = "us-central1-c"
}