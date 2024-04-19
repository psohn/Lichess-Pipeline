variable "location" {
  description = "Location"
  type = string
  default = "us-east1"
}

variable "project" {
  description = "Project"
  type = string
  default = "lichessdtc"
}

variable "gcs_bucket_name" {
  description = "GCS Bucket Name"
  type = string
  default = "lichess_dtc_bucket"
}

variable "bq_dataset_name" {
  description = "Bigquery Dataset Name"
  type = string
  default = "lichessdtc_lichess"
}

variable "region" {
  description = "Region"
  type = string
  default = "us-east1"
}

variable "credentials" {
  description = "GCP credentials"
  type = string
  default = "C:/Users/sohnp/Desktop/Lichess-Pipeline/mage/lichess_gcp.json"
}