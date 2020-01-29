import requests
import re

#retorna a url da foto do boobs para a função boobs
def get_url_boobs():
	contents = requests.get('http://api.oboobs.ru/boobs/0/1/random').json()
	url = contents[0]['preview']
	return url

#função que envia a foto do boobs pelo bot do telegram
def boobs(update, context):
	url = "http://media.oboobs.ru/"+get_url_boobs()
	chat_id = update.message.chat_id
	context.bot.send_photo(chat_id=chat_id, photo=url)	
	
