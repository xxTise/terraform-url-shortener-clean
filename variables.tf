variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "urlShortenerFunction"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table"
  type        = string
  default     = "url_shortener_table"
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}
