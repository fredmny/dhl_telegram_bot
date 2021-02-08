# Module to Load Shipment Inf

import os
import requests
from dotenv import load_dotenv

# Import Environmental variables
DHL_TOKEN = os.environ['DHL_API_TOKEN']

# Get shipment info

def get_shipment_info(tracking_number):

    params = {'trackingNumber': tracking_number}

    headers = {
        'Accept': 'application/json', 
        'DHL-API-Key': DHL_TOKEN
    }

    response = requests.get(
        'https://api-eu.dhl.com/track/shipments',
        params=params, 
        headers=headers
    )

    data = response.json()

    if response.status_code == 200:
        sh_timestamp = data['shipments'][0]['status']['timestamp']
        sh_status = data['shipments'][0]['status']['status']
        sh_description = data['shipments'][0]['status']['description']
        info = (response.status_code, sh_timestamp, sh_status, sh_description)
    else:
        info = response.status_code
    return info