# encoding: utf-8

import telegram
import configparser
import redis
from telegram.ext import Updater, CommandHandler

from telegram.ext import Updater

'''
# Configuring bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

# Connecting to Telegram APIs
# Updater retrieves information and dispatcher connects commands
updater = Updater(token=config['DEFAULT']['token'])
dispatcher = updater.dispatcher

# Connecting to Redis db
db = redis.StrictRedis(host=config['DB']['host'],
                       port=config['DB']['port'],
                       db=config['DB']['db'])
'''

#Connecting to Telegram API
#Updater retrieves information and dispatcher connects commands
updater = Updater(token='689972309:AAFqQeyPnJJn7tEW6W6FdA_ZT1QSyRKz9ls')
dispatcher = updater.dispatcher
# Connecting to Redis db
db = redis.StrictRedis(host='localhost',
                       port=6379,
                       db=0)
def start(bot, update):
    """
       Imprimindo mensagem de boas vindas e apresentando os possiveis comandos.
    """
    me = bot.get_me()

    # Welcome message
    msg = "Bem vindo!\n"
    msg += "O {0} está a sua disposição.\n".format(me.first_name)
    msg += "O que você deseja fazer?\n\n"
    msg += "/list - Listar os comandos\n"

    # Commands menu
    main_menu_keyboard = [[telegram.KeyboardButton('/list')]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)

'''
    A funcao CommandHandler liga um comando do usuario a uma funcao python
'''
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)