import logging
import requests
import re


def get_url_boobs():
	contents = requests.get('http://api.oboobs.ru/boobs/0/1/random').json()
	url = contents[0]['preview']
	return url


def boobs():
	url = "http://media.oboobs.ru/"+get_url_boobs()
	print("Testeboobs")
	print(url)
	
boobs()