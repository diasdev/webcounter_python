provider "aws" {
}

variable "instance_class" {
  type = string
  default = "db.t3.micro"
}

variable "db_name" {
  type = string
  default = "data"
}

variable "db_user" {
  type = string
  default = "user"
}

variable "db_password" {
  type = string
  default = "password"
}

variable "db_snapshot_id" {
  type = string
  default = null
}

resource "aws_db_subnet_group" "default" {
  subnet_ids = ["subnet-01389e54181db578d", "subnet-0cf35742acf3331bf"]
}

resource "aws_db_instance" "default" {
  allocated_storage    = 10
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = var.instance_class

  port     = 3306

  db_name  = var.db_name
  username = var.db_user
  password = var.db_password

  #lifecycle {
  #	prevent_destroy = true
  # }

  parameter_group_name = "default.mysql5.7"
  db_subnet_group_name = "${aws_db_subnet_group.default.id}"
  skip_final_snapshot  = true
  snapshot_identifier = var.db_snapshot_id

  lifecycle {
    ignore_changes = [snapshot_identifier]
  }
}
