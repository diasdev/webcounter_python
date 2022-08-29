output "db_host" {
  description = "The address of the RDS instance"
  value = aws_db_instance.default.address
}
