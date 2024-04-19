terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.14.0"
    }
  }
}

provider "google" {
  credentials = var.credentials
  project = var.project
  region = var.region
}

resource "google_storage_bucket" "lichess_dtc_bucket" {
  name = var.gcs_bucket_name
  location = var.location
  force_destroy = true
}

resource "google_bigquery_dataset" "lichess_dtc_dataset" {
  dataset_id = var.bq_dataset_name
  description = "Lichess DTC Dataset"
  location = var.location
  delete_contents_on_destroy = true
}