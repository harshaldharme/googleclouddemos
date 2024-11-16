variable "project_id" {
  description = "The GCP project ID"
  type        = string
  default     = "savvy-parser-441207-g9"
}

variable "function_region" {
  description = "The region where the Cloud Function will be deployed"
  type        = string
  default     = "us-central1" # Default to us-central1 region, can be changed
}

variable "function_name" {
  description = "The name of the Cloud Function"
  type        = string
  default     = "delete-resources-function"
}