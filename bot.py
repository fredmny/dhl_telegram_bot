''' Bot to send package information 
from DHL to my Telegram account'''
import os
import requests
from dotenv import load_dotenv

# Load own modules
import shipment_info

# Import Environmental variables
load_dotenv()
BOT_KEY = os.getenv('BOT_KEY')
TRACKN = os.getenv('TRACKING_NUMBER')

# Get the Shimpent Info
sh_info = shipment_info.get_shipment_info(TRACKN)

print(sh_info)


''' 
To Do:
- Turn timestamp info into individual variables
- Create Telegram Bot 
- run bot on startup / specific times

Info:
- https://developer.dhl.com/api-reference/shipment-tracking#reference-docs-section
- https://rapidapi.com/blog/how-to-use-an-api-with-python/ 
'''