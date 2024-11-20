variable "runtime" {
  description = "Runtime for the Cloud Function"
}

variable "function_name" {
  description = "Name of the Cloud Function"
}

variable "bucket" {
  description = "Source bucket name"
}

variable "zip_object" {
  description = "Source zip object"
}

variable "schedule" {
  description = "Cron schedule for Cloud Scheduler"
}

resource "google_cloudfunctions_function" "http_function" {
  name                  = var.function_name
  runtime               = var.runtime
  available_memory_mb   = 128
  source_archive_bucket = var.bucket
  source_archive_object = var.zip_object
  entry_point           = "delete_resources"
  trigger_http          = true
  https_trigger_security_level = "SECURE_ALWAYS"
}

resource "google_cloud_scheduler_job" "function_schedule" {
  name        = "${var.function_name}-schedule"
  description = "Schedule to trigger the cloud function at 2 AM UTC"
  schedule    = var.schedule
  time_zone   = "UTC"

  http_target {
    uri         = google_cloudfunctions_function.http_function.https_trigger_url
    http_method = "GET"

    oidc_token {
      service_account_email = google_cloudfunctions_function.http_function.service_account_email
    }
  }
}