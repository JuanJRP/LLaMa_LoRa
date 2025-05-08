import telebot
import os
import test

bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start', 'inicio', 'ayuda'])
def send_welcome(message):
	bot.reply_to(message, "Development by JuanJRP")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	response = test.preguntar(message.text)
	bot.reply_to(message, response)

bot.infinity_polling()
