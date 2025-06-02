import json
import os
import string
import random
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "")
    path_params = event.get("pathParameters") or {}

    if method == "POST":
        try:
            body = json.loads(event.get("body", "{}"))
            original_url = body.get("original_url")
            if not original_url:
                raise ValueError("original_url is required")
        except Exception as e:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": str(e)})
            }

        short_url = generate_short_url()
        table.put_item(Item={
            "short_url": short_url,
            "original_url": original_url
        })

        return {
            "statusCode": 200,
            "body": json.dumps({
                "short_url": short_url,
                "original_url": original_url
            })
        }

    elif method == "GET":
        short_url = path_params.get("short_url")
        if not short_url:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "short_url path parameter is required"})
            }

        response = table.get_item(Key={"short_url": short_url})
        item = response.get("Item")

        if not item:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Short URL not found"})
            }

        return {
            "statusCode": 301,
            "headers": {
                "Location": item["original_url"]
            },
            "body": ""
        }

    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method Not Allowed"})
        }
