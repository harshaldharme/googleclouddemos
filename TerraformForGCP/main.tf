provider "google" {
  project     = var.project
  credentials = file(var.credentials_file)
  region      = var.region
  zone        = var.zone
}

module "bigquery" {
  source = "./BigQuery"
  # project = var.project
}

module "cloud_function" {
  source = "./CloudFunction"
  # project = var.project
}