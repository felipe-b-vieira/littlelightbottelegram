from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re


def get_url_auau():
	contents = requests.get('https://random.dog/woof.json').json()
	url = contents['url']
	return url

def get_url_boobs():
	contents = requests.get('http://api.oboobs.ru/boobs/0/1/random').json()
	url = contents[0].contents['preview']
	return url


def boobs(bot, update):
	url = "http://media.oboobs.ru/"+get_url_boobs()
	url = get_url_auau()
	chat_id = update.message.chat_id
	bot.send_message(chat_id=chat_id, text=url)
	bot.send_photo(chat_id=chat_id, photo=url)	
	print("Testeboobs")
	
def auau(bot, update):
	url = get_url_auau()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)
	print("Testeauau")

def main():
	updater = Updater('704579297:AAH5MQ6dH-6dWDovssxRb0T1rcu4CS6DZpQ',use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('auau',auau))
	dp.add_handler(CommandHandler('boobs',boobs))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()