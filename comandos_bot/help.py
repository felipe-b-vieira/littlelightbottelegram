
#função que irá ajudar quem estiver falando com o bot, provavelmente irá listar os comandos
def help(update, context):
	"""Send a message when the command /help is issued."""
	update.message.reply_text('Help!')
