''' Bot to send package information 
from DHL to my Telegram account'''
import os
import requests
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Load own modules
import shipment_info

# Import Environmental variables
load_dotenv()
BOT_KEY = os.getenv('BOT_KEY')
TRACKN = os.getenv('TRACKING_NUMBER')

# Enable Logging
logging.basicConfig()

logger = logging.getLogger(__name__)

def start(update, context):
    # Send a message when the command /start is issued.
    update.message.reply_text('Welcome to the DHL Telegram bot')

def help(update, context):
    # Send a message when the command /help is issued.
    update.message.reply_text('Help!')

def error(update, context):
    # Log errors caused by Updates.
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Get the Shimpent Info
def shipment_status(update, context):
    sh_info = shipment_info.get_shipment_info(TRACKN)
    update.message.reply_text(
    f'--- Shipment Status ---\n\
    Last update: {sh_info[1]}\n\
    Status: {sh_info[2]}\n\
    Message: {sh_info[3]}'
    )

def main():
    '''
    Start the bot
    '''
    updater = Updater(BOT_KEY)

    # Get the dispatcher to register handlers (need to understand better)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('status', shipment_status))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

''' 
To Do:
- Turn timestamp info into individual variables
- Create Telegram Bot 
- run bot on startup / specific times

Info:
- https://developer.dhl.com/api-reference/shipment-tracking#reference-docs-section
- https://rapidapi.com/blog/how-to-use-an-api-with-python/ 
'''