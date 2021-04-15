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
## Locally:
# load_dotenv()
# BOT_KEY = os.getenv('BOT_KEY')
# TRACKING_NUMBER = os.getenv('TRACKING_NUMBER')
# APP_NAME = os.getenv('APP_NAME')

## On Heroku:
BOT_KEY = os.environ['BOT_KEY']
TRACKING_NUMBER = os.environ['TRACKING_NUMBER']
APP_NAME = os.environ['APP_NAME']
PORT = os.environ['PORT']

# Enable Logging
logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def help(update, context):
    # Send a message when the command /help is issued.
    help_message = (
        'Available commands',
        '/start - Start interaction with bot',
        '/status "tracking number" - Display tracking status',
        '/help - Display this help message'
    )
    update.message.reply_text('\n'.join(help_message))

def start(update, context):
    # Send a message when the command /start is issued.
    update.message.reply_text('Welcome to the DHL Telegram bot')
    
    help_message = (
        'Available commands',
        '/start - Start interaction with bot',
        '/status "tracking number" - Display tracking status',
        '/help - Display this help message'
    )
    update.message.reply_text('\n'.join(help_message))
    
def error(update, context):
    # Log errors caused by Updates.
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Get the Shimpent Info
def shipment_status(update, context):
    user_input = context.args
    if len(user_input) == 1:
        sh_info = shipment_info.get_shipment_info(user_input[0])
        if sh_info[0] == 200:
            update.message.reply_text(
            f'--- Shipment Status ---\nMessage: {sh_info[3]}'
            )
        else:
            update.message.reply_text(
                'Tracking number not found!'
            )
    else:
        error_reply = (
            'Please input just and only 1 Tracking Number.',
            f'You inputed {len(user_input)}.'
        )
        update.message.reply_text('\n'.join(error_reply))

def main():
    '''
    Start the bot
    '''

    updater = Updater(token=BOT_KEY)

    # Get the dispatcher to register handlers (need to understand better)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('status', shipment_status))

    dp.add_error_handler(error)

    # Using webhooks instead of polling. To test the code locally, comment the
    # two next functions and uncomment 'updater.start_polling()
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_KEY,
    )
    updater.bot.set_webhook(APP_NAME + BOT_KEY)
    
    # updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

''' 
To Do:
- Turn timestamp info into individual variables
- run bot on startup / specific times

Info:
- https://developer.dhl.com/api-reference/shipment-tracking#reference-docs-section
- https://rapidapi.com/blog/how-to-use-an-api-with-python/ 
'''