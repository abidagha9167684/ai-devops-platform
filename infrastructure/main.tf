terraform {
  required_version = ">= 1.0"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "project_info" {
  filename = "${path.module}/project-info.txt"

  content = <<-EOT
  Project: AI DevOps Platform
  Managed by: Terraform
  Environment: Dev
  EOT
}