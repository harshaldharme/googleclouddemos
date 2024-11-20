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

# Create a bucket to store function source code
resource "google_storage_bucket" "function_source_bucket" {
  name     = "function-source-bucket-delete-resources"
  location = var.region
}

# Upload zip file containing the function source code
resource "google_storage_bucket_object" "function_source_zip" {
  name   = "function-source.zip"
  bucket = google_storage_bucket.function_source_bucket.name
  source = "${path.module}/CloudFunction/delete_resources_function/function-source.zip"
}

# Call the CloudFunction module
module "cloud_function" {
  source                 = "./CloudFunction"
  function_name          = var.function_name
  runtime                = var.runtime
  bucket                 = google_storage_bucket.function_source_bucket.name
  zip_object             = google_storage_bucket_object.function_source_zip.name
  schedule               = var.schedule
}