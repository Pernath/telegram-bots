# -*- coding: utf-8 -*-
import os
from flask import Flask, request
import telebot
import logging
#cosas p
import schedule
import time
#import threading
from bs4 import BeautifulSoup
import requests
import random
import re

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

@bot.message_handler(regexp='[a-zA-Z]*')
def send_gif(message):
    if 'nudes' in message.text and (message.chat.id == -111035766 or message.from_user.username == "LumaEmu"):
        bot.reply_to(message, "Ese bot ShowNudes me la pela... Estoy tratando de conseguir material más nuevo y primitivo para ti... :v")
        bot.send_document(message.chat.id, choose_gif())
        try:
            bot.send_document(message.chat.id, parse_fallback("https://www.sex.com/gifs/?sort=popular&sub=week"))
        except:
            bot.reply_to(message, "Fallé miserablemente.")

@bot.message_handler(regexp='[a-zA-Z]*[\?]')
def mau_func(message):
    global count_msg
    # sorry buddy
    if count_msg < 4:
        #bot.reply_to(message, "La respuesta es: NO")
        count_msg += 1
    else:
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

'''
def lobo():
    bot.send_message(-162404891, "Las 12 pm no son las 12 de la noche")
def lobo_schedule():
    schedule.every().day.at("17:40").do(lobo)
while True:
    schedule.run_pending()
    time.sleep(1)
t = threading.Thread(name='hilo_basura', target=lobo_schedule)
t.start()
'''

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://maubot.herokuapp.com/bot")
    return "!", 200

def parse_fallback(pagina):
    r = requests.get(pagina)
    data = r.text
    # Creamos el objeto soup y le pasamos lo capturado con request
    soup = BeautifulSoup(data, 'lxml')    
    titulo = soup.title.text
    #import pdb; pdb.set_trace()
    print(titulo)
    #filtrado de img y gifs
    todas = soup.findAll("img", {"data-src":re.compile('\d+\.gif$')})#soup.find_all('img',src=re.compile('\d+\.gif$'))
    if not todas:
        return "https://images.sex.com/images/pinporn/2019/03/03/460/20770858.gif"
    a = random.randint(0,len(todas))
    out = todas[a]['data-src']
    if not out:
        out = "https://images.sex.com/images/pinporn/2019/03/03/460/20770858.gif"
    return out

def choose_gif():
    l = {0:"http://filthygifs.tumblr.com/",1:"http://nsfwgifland.tumblr.com/",2:"http://madporngifs.tumblr.com/", 
         4:"http://nsfwgifs.tumblr.com/",5:"http://www.poringa.net/posts/imagenes/2520377/Gifs-de-la-tetona-Hitomi-Tanaka.html", 6:"https://notwinterwind.tumblr.com/", 7:"http://dopeunsafe.tumblr.com/", 8:"http://nice-porno.tumblr.com/", 9:"http://selfienudes.club/", 10:"http://animated-gifs-for-everyone.tumblr.com/", 11:"http://thespaniard70.tumblr.com/", 12:"http://dirty-mind-fun-time.tumblr.com/", 13:"https://fullsexmachine.tumblr.com/", 14:"http://2drool4.tumblr.com/", 15:"http://filthygifs.tumblr.com/", 16:"http://hacky-gif.tumblr.com/", 17:"https://nakedchicksnstuff.tumblr.com/", 18:"https://nakedchicksnstuff.tumblr.com/post/158397736738", 19:"http://italiansd0itbetter.tumblr.com/", 20:"https://sexlibris.tumblr.com/", 21:"https://beautiesandthebreast.tumblr.com/", 22:"http://www.poringa.net/posts/gif/2070901/Megapost-Gifs-Porno.html", 23:"http://www.poringa.net/posts/gif/2159613/Gifs-para-romperse-el-brazo-Megapost.html", 24:"http://www.poringa.net/posts/imagenes/1993420/Megapost-Gifs-Porno-Clasif-Sexy-a-Porno.html", 25:"http://www.poringa.net/posts/gif/2677184/MegaPost-Gifs---Colas-Perfectas.html", 26:"http://www.poringa.net/posts/imagenes/2324604/Mega-Post-Gifs-Porno-1.html", 27:"http://www.poringa.net/posts/imagenes/2362764/Megapost-Gifs-pornos-2013.html", 28:"http://www.poringa.net/posts/imagenes/2520790/Megapost-de-Gifs-variados-mi-coleccion.html", 29:"http://www.poringa.net/posts/imagenes/2189401/Megapost-de-gif-calientes-poringueros.html", 30:"http://www.poringa.net/posts/imagenes/2198493/Gifs-Porno-Prohibidos-en-T-Megapost.html"}
    a = random.randint(0,len(l)-1)
    print("LOG: intento escoger de %s",l[a])
    pagina = (l[a])

    r = requests.get(pagina)
    data = r.text
    # Creamos el objeto soup y le pasamos lo capturado con request
    soup = BeautifulSoup(data, 'lxml')    
    titulo = soup.title.text
    
    print(titulo)
    #filtrado de img y gifs
    todas = soup.find_all('img',src=re.compile('\d+\.gif$'))
    a = random.randint(0,len(todas)-1)
    out = todas[a]['src']
    print(out)
    return out


server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)


#bot.polling()
