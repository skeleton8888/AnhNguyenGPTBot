import os
import openai
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

openai.api_key = "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"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def chat(update, context):
    """Echo the user message."""
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt="User: " + update.message.text + "\nBot: ",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    ).choices[0].text
    update.message.reply_text(response)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(Message