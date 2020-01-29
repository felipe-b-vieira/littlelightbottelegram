
#função start do telegram, deve ser responsável por iniciar o bot antes de qualquer coisa
def start(update, context):
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Hi!')
