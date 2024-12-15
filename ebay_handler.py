import requests
import os
import json

# Environment variables (set in Lambda console)
EBAY_OAUTH_TOKEN = os.getenv('EBAY_OAUTH_TOKEN')
BASE_URL = 'https://api.sandbox.ebay.com/sell/inventory/v1'

def create_inventory_item(oauth_token, item_details):
    """Creates an inventory item on eBay."""
    if not oauth_token:
        raise ValueError("OAuth token is missing.")

    sku = item_details["sku"]
    url = f"{BASE_URL}/inventory_item/{sku}"
    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Language": "en-US"
    }


    try:
        response = requests.put(url, headers=headers, json=item_details)
        if response.status_code == 201:
            return sku
        elif response.status_code == 204:
            return sku
        else:
            raise Exception(f"Error creating inventory item: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")

def create_offer(oauth_token, offer_details):
    """Creates an offer for an existing inventory item."""
    if not oauth_token:
        raise ValueError("OAuth token is missing.")

    url = f"{BASE_URL}/offer"
    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Language": "en-US"
    }

    try:
        response = requests.post(url, headers=headers, json=offer_details)
        if response.status_code == 201:
            offer_data = response.json()
            return offer_data.get('offerId', None)
        else:
            raise Exception(f"Error creating offer: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")

def ebay_request_processor(event, context):
    """AWS Lambda handler function."""
    if not EBAY_OAUTH_TOKEN:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: OAuth token not found.')
        }

    try:
        # Ensure event['body'] is parsed as a JSON string first if it's coming as a JSON string
        data = json.loads(event['body'])  # Expecting the body to be a JSON string

        item_details = data.get('itemDetails', {})
        offer_details = data.get('offerDetails', {})

        if not item_details or not offer_details:
            return {
                'statusCode': 400,
                'body': json.dumps('Error: Missing item details or offer details in the event payload.')
            }

        # Create inventory item
        sku = create_inventory_item(EBAY_OAUTH_TOKEN, item_details)

        if sku:
            # Add SKU to the offer details
            offer_details["sku"] = sku

            # Create the offer
            offer_id = create_offer(EBAY_OAUTH_TOKEN, offer_details)

            if offer_id:
                return {
                    'statusCode': 200,
                    'body': json.dumps(f"Offer created successfully! Offer ID: {offer_id}")
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Failed to create offer.')
                }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Failed to create inventory item.')
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal Server Error: {str(e)}")
        }
