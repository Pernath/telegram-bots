# -*- coding: utf-8 -*-
import os
from flask import Flask, request
import telebot
import logging
#cosas p
import schedule
import time
import threading

token = '245656240:AAG5LmYWt88UEGPh6uIH9O61HGA94QvM9xY'
bot = telebot.TeleBot(token)
server = Flask(__name__)
lista = []
count_msg = 0



logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Mi nombre es Mauricio y soy un bot. He venido desde el espacio proyectivo complejo para hacerte la vida un poquito complicada ;)")

@bot.message_handler(regexp='[a-zA-Z]*[\?]')
def mau_func(message):
    global count_msg
    '''
    if count_msg < 4:
        bot.reply_to(message, "La respuesta es: NO")
        count_msg += 1
    else:
    '''
    if count_msg == 7:
        bot.send_message(message.chat.id, "La gente está muy confundiiiiidaaaaaa...")
        count_msg = 0
    else:
        count_msg += 1
        

@bot.message_handler(func=lambda m: True)
def answer_ray_dian(message):
    if message.from_user.username == "RayHyde" and count_msg == 2:
        bot.reply_to(message, "Ya pon el server, Ray")
    if message.from_user.username == "Dianagr":
        bot.reply_to(message, "Me agüitas, Daiana...")

@bot.message_handler(func=lambda m: True)
def random_reply(message):
    pass

# Se prueba el viernes 11 de noviembre
def lobo():
    bot.send_message(-162404891, "Las 12 pm no son las 12 de la noche")
def lobo_schedule():
    schedule.every().day.at("17:40").do(lobo)
    while True:
        schedule.run_pending()
        time.sleep(1)
t = threading.Thread(name='hilo_basura', target=lobo_schedule)
t.start()

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://maubot.herokuapp.com/bot")
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)


#bot.polling()
