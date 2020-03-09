import requests
import re
import Algorithmia


#algoritmo de sumario usado
client = Algorithmia.client(keyAlgorit)
algo = client.algo('nlp/Summarizer/0.1.3')


#função que resume a mensagem enviada
def resumo(update, context):
	url = get_url_auau()
	chat_id = update.message.chat_id
	context.bot.send_photo(chat_id=chat_id, photo=url)