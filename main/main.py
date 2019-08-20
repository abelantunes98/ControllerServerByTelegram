# encoding: utf-8
import sys
import os
import telegram
import configparser
import redis
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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
# Timeout modificado
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
    print("Iniciou!")
    me = bot.get_me()

    # Welcome message
    msg = "Bem vindo!\n"
    msg += "O {0} está a sua disposição.\n".format(me.first_name)
    msg += "O que você deseja fazer?\n\n"
    msg += "/reboot - Reiniciar sistema.\n"
    msg += "/download - Efetuar downloads.\n"
    msg += "/stop - Parar servidor."

    # Commands menu
    main_menu_keyboard = [[telegram.KeyboardButton('/reboot')],
                            [telegram.KeyboardButton('/download')], [telegram.KeyboardButton('/stop')]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)

def reboot(bot, update):
    msg = "Efetuando Reboot..."

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg
                     )

    os.system("shutdown -r now")


def download(bot, update):
    main_menu_keyboard = [[telegram.KeyboardButton('/video')]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                one_time_keyboard=True)
    msg = "Selecione a opção de Download:\n"
    msg += "/video"
    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)

def download_video(bot, update):
    msg = "Informe a url do video desejado no formato {/ url} e aguarde um pouco."
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def send_video(bot, update):
    try:
        # supports_streaming=True
        videoDec = open('videos/video.mp4', 'rb')
        bot.sendVideo(chat_id = update.message.chat_id, video = videoDec)
    except Exception as e:
        print(e)
        msg = "Upando video..."
        bot.send_message(chat_id=update.message.chat_id, text=msg)
        upload_video("videos/video.mp4", bot, update)

def upload_video(video_name, bot, update):
    comando = "bash upVideo.sh"
    try:
        os.system(comando)
        msg = "Video upado!"
        bot.send_message(chat_id=update.message.chat_id, text=msg)
    except Exception as e:
        print(e)
        msg = "Erro ao upar video..."
        bot.send_message(chat_id=update.message.chat_id, text=msg)


def stop():
    """
        Funcao que desliga o servidor
    """
    os.system("bash /pw/stop.sh")
def unknown(bot, update):
    """
        Placeholder command when the user sends an unknown command.
    """

    if (update.message.text[1] != " "):
        msg = "Esse comando não é reconhecido pelo sistema!"
        bot.send_message(chat_id=update.message.chat_id, text=msg)
    else:
        try:
            video_url = update.message.text.split()[1]
            arquivo = open('url.txt', 'w')
            arquivo.write(video_url)
            arquivo.close()
            comando = "nohup bash downloadVideo.sh > /dev/null &"
            os.system(comando)
            '''comando = " youtube-dl -o \"/usr/bin/usr/tel/videos/%(title)s.%(ext)s\" " + video_url
            os.system(comando)
            comando = "ls videos/ > nome.txt"
            os.system(comando)
            comando = "mv videos/\"$(cat nome.txt)\" videos/video.mp4"
            os.system(comando)'''
            #send_video(bot, update)
            #comando = "rm videos/video.mp4 nome.txt"
            #os.system(comando)
        except Exception as e:
            print(e)

'''
    A funcao CommandHandler liga um comando do usuario a uma funcao python
'''
start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)
reboot_handler = CommandHandler('reboot', reboot)
download_handler = CommandHandler('download', download)
download_video_handler = CommandHandler('video', download_video)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(reboot_handler)
dispatcher.add_handler(download_handler)
dispatcher.add_handler(download_video_handler)

unknown_handler = MessageHandler([Filters.command], unknown)
dispatcher.add_handler(unknown_handler)