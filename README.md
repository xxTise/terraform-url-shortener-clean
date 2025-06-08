
# 🔗 Serverless URL Shortener – Built with AWS & Terraform

Create short, shareable links with automatic 301 redirects – powered entirely by AWS Lambda, API Gateway, and DynamoDB, all provisioned with Terraform. ⚡️

> Built by [Tise Ogundeji](https://www.linkedin.com/in/tise-ogundeji-a08890246), a Cloud Engineer-in-the-making.

---

## 🌍 Live API Demo

👉 **POST**: `https://<your-api-id>.execute-api.us-east-1.amazonaws.com/`  
👉 **GET**: `https://<your-api-id>.execute-api.us-east-1.amazonaws.com/{short_url}`

Replace `<your-api-id>` with the actual API ID Terraform outputs after deployment.

---

## 🚀 Features

- 🔐 **Serverless Infrastructure** – Zero servers to manage, auto-scaled.
- 🔁 **301 Redirects** – Proper HTTP redirection using API Gateway & Lambda.
- ⚙️ **Infrastructure as Code** – Built, deployed, and managed entirely with Terraform.
- 🪵 **Cloud-native Logging** – Real-time logs via AWS CloudWatch.
- ⚡ **Fast DynamoDB Reads/Writes** – PAY_PER_REQUEST billing, no over-provisioning.

---

## 🧱 Architecture Overview

```
[POST /] + [GET /{short_url}]
        │
    API Gateway HTTP API
        │
   AWS Lambda Function (Python)
        │
    Amazon DynamoDB Table
```

- **API Gateway** handles incoming HTTP requests.
- **Lambda** handles logic to shorten and resolve URLs.
- **DynamoDB** stores short → long URL mappings.

---

## 💻 Usage

### 🔨 POST `/` — Create a short URL

**Request**

```http
POST /
Content-Type: application/json

{
  "original_url": "https://example.com"
}
```

**Response**

```json
{
  "short_url": "MtGNFy",
  "original_url": "https://example.com"
}
```

---

### 🌐 GET `/{short_url}` — Redirect to the original URL

**Request**

```http
GET /MtGNFy
```

**Response**

- HTTP Status: `301 Moved Permanently`
- Redirects to: `https://example.com`

---

## 📁 Project Structure

```
terraform-url-shortener/
├── lambda/
│   └── handler.py               # Lambda function (Python 3.10)
├── lambda_function_payload.zip # Zipped Lambda package
├── main.tf                      # Terraform: Resources (API GW, Lambda, DynamoDB)
├── variables.tf                 # Input variables
├── outputs.tf                   # Output values
├── providers.tf                 # AWS provider config
├── .gitignore                   # Ignored files/folders
└── README.md                    # This file!
```

---

## 📦 Requirements

- Terraform ≥ 1.0
- AWS CLI configured
- Python 3.10
- An AWS account with sufficient IAM permissions

---

## 🧪 Deployment Steps

1. **Zip the Lambda code**

```bash
cd lambda
zip ../lambda_function_payload.zip handler.py
cd ..
```

2. **Initialize Terraform**

```bash
terraform init
```

3. **Apply the config**

```bash
terraform apply
```

4. **Grab the API URL from output and test**

---

## 🔮 Future Improvements

- [ ] Custom slugs (e.g. `/tise`)
- [ ] URL expiry / TTL
- [ ] Analytics: Click count, source, timestamp
- [ ] Auth for URL management
- [ ] Frontend for URL generation

---

## 👨🏽‍💻 Author

**Tise Ogundeji**  
Cloud Engineer | Entrepreneur | AWS Enthusiast  
🌍 [LinkedIn](https://www.linkedin.com/in/tise-ogundeji-a08890246)  
🐙 [GitHub](https://github.com/xxTise)

---

## 🏁 Final Words

This project demonstrates real-world skills in:

✅ Cloud Architecture  
✅ Serverless Computing  
✅ Infrastructure as Code (IaC)  
✅ Python + AWS SDK (Boto3)  
✅ REST API development

> If you're hiring or collaborating — let's connect!
