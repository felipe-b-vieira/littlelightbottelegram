import requests
import re
from random import randint

#função que te da 1/6 chance de ser kickado do chat, só funciona contra não admins e se o bot for admin
def roletaKick(update, context):
	usuarioAtual = update.message.from_user
	idUsuario =usuarioAtual.id
	chat_id = update.message.chat_id
	#roda o valor, se 1 é morte
	tiro = randint(1,6)
	if(tiro==1):
		sucesso = context.bot.kick_chat_member(chat_id,idUsuario)
		if(not sucesso):
			update.message.reply_text("Problema ao kickar, por favor, verificar se as condições para funcionamento estão corretas.")
	else:
		update.message.reply_text("Você sobreviveu.")
	
