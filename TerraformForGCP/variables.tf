variable "project" {

}

variable "credentials_file" {

}

variable "region" {
  default = "us-central1"
}

variable "zone" {
  default = "us-central1-c"
}

variable "os_image" {
  default = "debian-cloud/debian-11"
}

variable "enable_vm" {
  type    = bool
  default = false
}

variable "vm_params" {
  type    = tuple([string, string, bool])
  default = ["f1-micro", "us-central1-c", true]
}

variable "count_demo_gce_names" {
  type    = list(string)
  default = ["instance-1", "instance-2"]
}

variable "element_demo_vm_tags" {
  type    = list(string)
  default = ["first-tag", "second-tag"]
}

variable "project_id" {
  description = "Google Cloud project ID"
}

variable "function_name" {
  description = "Name of the Cloud Function"
  default     = "delete-resources-function"
}

variable "runtime" {
  description = "Runtime for the Cloud Function"
  default     = "python310"
}

variable "schedule" {
  description = "Schedule for the Cloud Function"
  default     = "0 2 * * *" # 2AM UTC daily
}