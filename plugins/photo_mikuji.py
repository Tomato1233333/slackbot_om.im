#coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import requests
import random
import os
from slackclient import SlackClient

bot_token = "BOT_TOKEN"
my_token = "MY_API_TOKEN"
#slack_token = os.getenv("SLACK_TOKEN")
sc = SlackClient(bot_token)

@respond_to('りんご')
def mention_func(message):
	with open("apple1.png",'rb') as f:
		param = {'token':bot_token,'channels':'CHANNEL_ID','title':'apple'}
		r = requests.post("https://slack.com/api/files.upload",params=param,files={"file":f})
	message.reply('りんごだよ!!僕はトマトが好きだけど!!')


@respond_to('トマト')
def mention_func(message):
	with open("tomato1.png","rb") as f:
		param = {'token':bot_token,'channels':'CHANNEL_ID','title':'tomato'}
		r = requests.post("https://slack.com/api/files.upload",params=param,files={"file":f})
	message.reply('トマト！！僕好きなんだ〜！')

@listen_to('おみくじ')
@listen_to('すたーと')
def listen_func(message):
	if sc.rtm_connect():
		while True:
			read = sc.rtm_read()
			if len(read) != 0:
				if read[0]['type'] == 'hello':
					pass
				if read[0]['type'] == "message": 
					if read[0]['user'] == "USER_ID":
						message.send('君のことは嫌いだからやらない.....')
						print(read)

					elif read[0]['user'] == "USER_ID":
						message.send('君Botでしょ？自分でやれば？')
						print(read)

					elif read[0]['user'] == "USER_ID":
						pass

					elif read[0]['user'] == "USER_ID":
						print(read)
						kettei = random.randint(1,5)
						kekka_list = ''
						omikuji = Omikuji(kettei,kekka_list)
						message.send(omikuji.kekka())

	else:
		print("Connection Failed")

class Omikuji:
	def __init__(self, kettei,list_kekka):	
		self.kettei = kettei
		self.list_kekka = list_kekka

	def kekka(self):
		if self.kettei == 1:
			self.list_kekka = "大吉だよ!!"
		if self.kettei == 2:
			self.list_kekka = "中吉だよ!!"
		if self.kettei == 3:
			self.list_kekka = "小吉だよ!!"
		if self.kettei == 4:
			self.list_kekka = "吉だよ!!"
		if self.kettei == 5:
			self.list_kekka = "悪いな！凶だ！"
		
		return self.list_kekka
