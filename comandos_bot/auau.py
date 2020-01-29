import requests
import re

#retorna a url da foto do cachorro para a função auau
def get_url_auau():
	contents = requests.get('https://random.dog/woof.json').json()
	url = contents['url']
	return url

#função que envia a foto de um cachorro pelo bot do telegram
def auau(update, context):
	url = get_url_auau()
	chat_id = update.message.chat_id
	context.bot.send_photo(chat_id=chat_id, photo=url)