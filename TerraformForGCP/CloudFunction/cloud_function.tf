
resource "google_storage_bucket" "function_source_bucket" {
  name     = "function-source-bucket-delete-resources"
  location = "US"
}

resource "google_storage_bucket_object" "function_source_code" {
  name   = "function-source.zip"
  bucket = google_storage_bucket.function_source_bucket.name
  source = "path/to/your/function-source.zip" # Path to your zipped function code
}

resource "google_cloudfunctions_function" "delete_resources" {
  name        = var.function_name
  description = "Cloud Function to delete resources at 2AM every day"
  runtime     = "python310"
  entry_point = "delete_resources"

  source_archive_bucket = google_storage_bucket.function_source_bucket.name
  source_archive_object = google_storage_bucket_object.function_source_code.name
  region                = var.function_region

  environment_variables = {
    PROJECT_ID = var.project_id
  }

  available_memory_mb = 256
  timeout             = 60

  # Trigger type: HTTP Trigger
  trigger_http = true
}

resource "google_cloud_scheduler_job" "delete_resources_job" {
  name        = "delete-resources-job"
  description = "Scheduler to trigger the Cloud Function every day at 2 AM"
  schedule    = "0 2 * * *" # This is 2 AM every day
  time_zone   = "UTC"

  http_target {
    uri = google_cloudfunctions_function.delete_resources.https_trigger_url
    http_method = "POST"
    headers = {
      "Content-Type" = "application/json"
    }
  }
}

# IAM Binding to allow Cloud Scheduler to invoke the function
resource "google_project_iam_member" "scheduler_invoker" {
  project = var.project_id
  role    = "roles/cloudfunctions.invoker"
  member  = "serviceAccount:cloudscheduler@${var.project_id}.iam.gserviceaccount.com"
}