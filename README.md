# Lambda-powered-eBay-Integration

![Project Type](https://img.shields.io/badge/Project-Type%3A%20Serverless%20Integration-blue)  
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)  
![Tools Used](https://img.shields.io/badge/Tools-Python%20%7C%20AWS%20Lambda%20%7C%20Serverless%20Framework%20%7C%20Requests%20%7C%20Boto3-orange)


A Python-based project leveraging AWS Lambda to automate the integration with eBay's Inventory API. This repository contains functionality for managing inventory items and creating offers on the eBay platform programmatically.

## Features

- **Inventory Management:** Create and manage inventory items on eBay.
- **Offer Creation:** Automate offer creation for existing inventory items.
- **Serverless Integration:** Built to run seamlessly on AWS Lambda.
- **Error Handling:** Includes robust error handling and logging mechanisms.

## File Overview

- **`ebay_handler.py`**: Core Lambda function script handling eBay API requests for inventory and offers.
- **`requirements.txt`**: Dependencies for the project.
- **`serverless.yml`**: Serverless Framework Configuration.
- **`test_evenet.json`**: Sample Test Payload.

## Prerequisites

Before using this project, ensure you have the following:

1. **AWS Lambda Setup**:
   - Create a Lambda function on AWS.
   - Configure environment variables:
     - `EBAY_OAUTH_TOKEN`: Your eBay OAuth token for API access.

2. **eBay Developer Account**:
   - Sandbox or production API credentials.
   - OAuth token generated via eBay Developer portal.

3. **Python Packages**:
   - Install dependencies locally or include in your deployment package:
     - `requests`
     - `json`

## Setup and Deployment

### 1. Clone the Repository
```bash
git clone https://github.com/gaganageethika/ebay-inventory-lambda.git
cd ebay-inventory-lambda
```
### 2. Update Environment Variables
Set your `EBAY_OAUTH_TOKEN` in the AWS Lambda environment settings.

### 3. Test Locally (Optional)
You can test the Lambda handler locally with tools like `AWS SAM` or `pytest`.

### 4. Deploy to AWS Lambda
Zip your project and deploy it to AWS Lambda:

```bash
zip -r lambda_function.zip ebay_handler.py
Upload lambda_function.zip to your Lambda function.
```

### 5. Invoke the Function
Send an event payload in the following format to the Lambda function:

```json
Copy code
{
  "body": "{\"itemDetails\": {\"sku\": \"item123\", \"details\": \"...\"}, \"offerDetails\": {\"price\": \"10.99\"}}"
}
```
## Example Use Case
- Automate eBay inventory creation for new products.
- Quickly list items with offers for various marketplaces.
- Scale serverless integration without maintaining dedicated servers.

##Contributing
Contributions are welcome! Feel free to fork the repository, submit issues, or open pull requests.

##License
This project is licensed under the MIT License. See LICENSE for more details.


### Guide to Setting Up Your Repository

1. **Initialize Git Repository**:
   ```bash
   git init
   ```
2. **Add Files**:
    Ensure ebay_handler.py and README.md are in the root directory.
3. **Commit and Push**:

```bash
git add .
git commit -m "Initial commit: eBay Lambda integration"
git branch -M main
git remote add origin https://github.com/yourusername/ebay-inventory-lambda.git
git push -u origin main
```
