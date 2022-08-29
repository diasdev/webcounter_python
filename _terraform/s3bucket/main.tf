provider "aws" {
}

variable "bucket_name" {
  type = string
  default = "example"
}

resource "aws_s3_bucket" "default" {
  bucket = var.bucket_name

  tags = {
    Name        = var.bucket_name
  }
}

resource "aws_s3_bucket_acl" default {
  bucket = aws_s3_bucket.default.id
  acl    = "private"
}

