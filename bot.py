''' Bot to send package information 
from DHL to my Telegram account'''
import os
import requests
from dotenv import load_dotenv

load_dotenv()
TRACKN = os.getenv('TRACKING_NUMBER')
TOKEN = os.getenv('DHL_API_TOKEN')

params = {'trackingNumber': TRACKN}

headers = {
    'Accept': 'application/json', 
    'DHL-API-Key': TOKEN
}

response = requests.get('https://api-eu.dhl.com/track/shipments',params=params, headers=headers)

print(response)

data = response.json()

sh_timestamp = data['shipments'][0]['status']['timestamp']
sh_status = data['shipments'][0]['status']['status']


''' 
To Do:
- Turn timestamp info into individual variables
- Create Telegram Bot 
- run bot on startup / specific times

Info:
- https://developer.dhl.com/api-reference/shipment-tracking#reference-docs-section
- https://rapidapi.com/blog/how-to-use-an-api-with-python/ 
'''