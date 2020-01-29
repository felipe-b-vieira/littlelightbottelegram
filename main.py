#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

#adiciona as pastas com os outros arquivos python
import sys
sys.path.insert(0,'./comandos_bot')

from auau import auau
from boobs import boobs
from start import start
from help import help
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
logger = logging.getLogger(__name__)

#variaveis inicias globais
token_telegram = os.environ.get('TOKENTELEGRAM', None)





def echo(update, context):
	"""Echo the user message."""
	update.message.reply_text(update.message.text)


def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	# Make sure to set use_context=True to use the new context based callbacks
	# Post version 12 this will no longer be necessary
	updater = Updater(token_telegram, use_context=True)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("auau", auau))
	dp.add_handler(CommandHandler("boobs", boobs))

	# on noncommand i.e message - echo the message on Telegram
	# dp.add_handler(MessageHandler(Filters.text, echo))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


	
	
if __name__ == '__main__':
	main()