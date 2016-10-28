import telebot
token = '245656240:AAG5LmYWt88UEGPh6uIH9O61HGA94QvM9xY'
bot = telebot.TeleBot(token)
lista = []
count_msg = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola soy un bot, mi nombre es Mauricio y vine a hacerte la vida un poquito complicada ;)")

@bot.message_handler(regexp='[a-zA-Z]*[\?]')
def mau_func(message):
    global count_msg
    if count_msg < 4:
        bot.reply_to(message, "La respuesta es: NO")
        count_msg += 1
    else:
        bot.reply_to(message, "La gente está muy confundiiiiidaaaaaa...")
        count_msg = 0

@bot.message_handler(func=lambda m: True)
def answer_ray_dian(message):
    if message.from_user.username == "RayHyde" and count_msg == 2:
        bot.reply_to(message, "Ya pon el server, Ray")
    if message.from_user.username == "Dianagr":
        bot.reply_to(message, "Me agüitas, Daiana...")

@bot.message_handler(func=lambda m: True)
def random_reply(message):
    pass
bot.polling()
