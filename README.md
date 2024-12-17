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
