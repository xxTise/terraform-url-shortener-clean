output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.url_shortener_lambda.function_name
}

output "dynamodb_table_name" {
  description = "The name of the DynamoDB table"
  value       = aws_dynamodb_table.url_shortener.name
}

output "api_url" {
  description = "API Gateway invoke URL"
  value       = aws_apigatewayv2_api.api.api_endpoint
}
