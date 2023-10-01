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

variable "vm_params" {
  type = tuple([ string, string, bool ])
  default = [ "f1-micro", "us-central1-c", true ]
}