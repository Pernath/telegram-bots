from telegram.ext import Updater
from telegram.ext import CommandHandler
import telebot
token = '267952977:AAHHmj0tNUMaAP7iytzfRpb02wkyAcF45UE'
#bot = telebot.TeleBot(token)
class Bot(object):
    def __init__(self):
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher
        self.lista = []

        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('help', self.start))
        self.dispatcher.add_handler(CommandHandler('nueva', self.nueva))
        self.dispatcher.add_handler(CommandHandler('todo', self.todo))
        self.dispatcher.add_handler(CommandHandler('agregar', self.agregar))
        self.dispatcher.add_handler(CommandHandler('borrar', self.borrar))
        self.dispatcher.add_handler(CommandHandler('ver', self.ver))
        self.dispatcher.add_handler(CommandHandler('quitar', self.quitar))

    def start(self,bot, update):
        bot.sendMessage(chat_id=update.message.chat_id,text="Hola, soy el bot que hizo Carlos :o")

    def nueva(self, bot, update):
        params = update.message.text.split();
        print(params)
        if len(params) > 1:
            if not self.exists(params[1]):
                self.lista.append(Lista(params[1]))
                bot.sendMessage(chat_id=update.message.chat.id,text="Nueva lista creada: "+params[1])
            else:
                bot.sendMessage(chat_id=update.message.chat.id,text="La lista "+params[2]+" no existe o el elemento "+params[1]+" ya existe en la lista")
        else:
            bot.sendMessage(chat_id=update.message.chat.id, text="Necesito el nombre de la nueva lista a crear")

    def todo(self,bot,update):
        if len(self.lista) > 0:
            bot.sendMessage(chat_id=update.message.chat.id,text=self.list())
        else:
            bot.sendMessage(chat_id=update.message.chat.id,text="Aún no hay ninguna lista")
    def agregar(self,bot,update):
        params = update.message.text.split();
        if len(params) > 2:
            b = 0
            try:
                b = int(params[1])
                if not addi(b, params[2]):
                    bot.sendMessage(chat_id=update.message.chat.id,text= params[2]+" ya existe en la lista o la lista "+params[1]+" no existe")
                else:
                    bot.sendMessage(chat_id=update.message.chat.id,text=params[2]+" agregado a "+params[1])
            except ValueError:
                if not add(params[1], params[2]):
                    bot.send_message(chat_id=update.message.chat.id,text=params[2]+" ya existe en la lista o la lista "+params[1]+" no existe")
                else:
                    bot.send_message(chat_id=update.message.chat.id, text=params[2]+" agregado a "+params[1])
    def add(self,nomlist, e):
        for x in self.lista:
            if x.__str__() == nomlist:
                return x.add(e)
        return False


    def addi(self,i, e):
        if i > len(self.lista)-1:
            return False
        return self.lista[i].add(e)

    def remove(self,nomlist, e):
        for x in self.lista:
            if x.__str__() == nomlist:
                return x.remove(e)
        return False

    def removei(self,nomlist, i):
        for x in self.lista:
            if x.__str__() == nomlist:
                return x.removei(i)
        return False

    def display(self,c):
        if c < len(self.lista):
            return self.lista[c].all()
        if c == -1:
            pass
        return "Ese índice no existe en la lista"

    def display2(self,string):
        for x in self.lista:
            if x.__str__() == string:
                return x.all()

    def exists(self,string):
        for x in self.lista:
            if x.__str__() == string:
                return True
        return False


    def ver(self,bot,update):
        params = update.message.text.split();
        print("quiere ver...")
        if len(params) > 1:
            b = 0
            try:
                b = int(params[1])
                bot.sendMessage(chat_id=update.message.chat.id,text=display(b))
            except ValueError:
                bot.send_message(chat_id=update.message.chat.id,text=display2(params[1]))
            else:
                bot.send_message(chat_id=update.message.chat.id,text="Necesito el índice o el nombre de la lista que quieres ver.\nPrueba de nuevo")
    def quitar(self,bot,update):
        params = update.message.text.split();
        if len(params) > 1:
            if borra(params[1]):
                bot.sendMessage(chat_id=update.message.chat.id,text="Lista "+params[1]+" eliminada")
            else:
                bot.sendMessage(chat_id=update.message.chat.id,text="Lista "+params[1]+" no se encuentra")
        else:
            bot.send_message(chat_id=update.message.chat.id,text="Necesito el nombre de la lista que quieres eliminar.\nPrueba de nuevo")
    def borra(self,elem):
        for x in self.lista:
            if x.__str__() == elem:
                self.lista.remove(x)
            return True
        return False

    def borrar(self,bot,update):
        params = update.message.text.split();
        if len(params) > 2:
            b = 0
            try:
                b = int(params[2])
                if removei(params[1],b):
                    bot.sendMessage(chat_id=update.message.chat.id,text=params[2]+" eliminado de "+params[1])
            except ValueError:
                if remove(params[1], params[2]):
                    bot.sendMessage(chat_id=update.message.chat.id, text=params[2]+" eliminado de "+params[1])
                else:
                    bot.sendMessage(chat_id=update.message.chat.id,text= "No se pudo borrar")
    def list(self):
        a = "Estas son las listas que tenemos :]\n"
        i = 0
        for x in self.lista:
            a += str(i)+") "+x.__str__()+"\n"
            i += 1
        return a

    def start_polling(self):
        self.updater.start_polling()
class Lista:
    add = False
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []

    def add(self, e):
        if not e in self.lista:
            self.lista.append(e)
            return True
        return False

    def remove(self, x):
        if x not in self.lista:
            return False
        self.lista.remove(x)
        return True

    def removei(self, i):
        if i > len(self.lista)-1:
            return False
        self.lista.remove(self.lista[i])
        return True

    def all(self):
        if len(self.lista) == 0:
            return "Lista vacía"
        a = "Lista: "+self.nombre+".-\n"
        i = 0
        for x in self.lista:
            a += str(i)+") "+x+"\n"
            i += 1
        return a

    def __str__(self):
        return self.nombre


if __name__ == '__main__':
    boot = Bot()
    boot.start_polling()
