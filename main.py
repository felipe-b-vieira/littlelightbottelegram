#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongoengine import *
import logging
import os

#adiciona as pastas com os outros arquivos python
import sys
sys.path.insert(0,'./comandos_bot')
sys.path.insert(0,'./controleUsuarios')

from auau import auau
from boobs import boobs
from start import start
#from briga import briga,adiciona_briga
from help import help
from controle_de_usuarios import salva_usuario
from medadinheiro import me_da_dinheiro
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
logger = logging.getLogger(__name__)

#variaveis inicias globais
token_telegram = os.environ.get('TOKENTELEGRAM', None)
user_mongodb = os.environ.get('USERMONGOATLAS', None)
pass_mongodb = os.environ.get('PASSWORDMONGOATLAS', None)
db_mongodb = os.environ.get('DBNAMEMONGODB', None)
cluster_name = os.environ.get('CLUSTERNAME', None)
cluster_code = os.environ.get('CLUSTERCODE', None)




def echo(update, context):
	"""Echo the user message."""
	update.message.reply_text(update.message.text)


def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)

	
def conectaDB():
	#connect( db=db_mongodb, username=user_mongodb, password=pass_mongodb, host=cluster_name+".gcp.mongodb.net")
	#print('mongodb+srv://'+user_mongodb+':'+pass_mongodb+'@'+cluster_name+'.gcp.mongodb.net/test?retryWrites=true&w=majority')
	connect(host='mongodb://'+user_mongodb+':'+pass_mongodb+'@'+cluster_name+'-shard-00-00-'+cluster_code+'.gcp.mongodb.net:27017,'+cluster_name+'-shard-00-01-'+cluster_code+'.gcp.mongodb.net:27017,'+cluster_name+'-shard-00-02-'+cluster_code+'.gcp.mongodb.net:27017/'+db_mongodb+'?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')


def main():
	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	# Make sure to set use_context=True to use the new context based callbacks
	# Post version 12 this will no longer be necessary
	updater = Updater(token_telegram, use_context=True)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	#conecta com o mongodbatlas
	conectaDB()
	
	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("auau", auau))
	dp.add_handler(CommandHandler("boobs", boobs))
	#dp.add_handler(CommandHandler("briga", briga))
	#dp.add_handler(CommandHandler("adiciona_briga", briga))
	dp.add_handler(CommandHandler("me_da_dinheiro", me_da_dinheiro))
	
	# vai ler os textos dos grupos cada vez que uma mensagem for mandada, verificar se já tenho todos os usuários do grupo salvo, senão, salvo o novo usuário
	dp.add_handler(MessageHandler(Filters.text, salva_usuario))

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