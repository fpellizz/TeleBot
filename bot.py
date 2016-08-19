import sys
import time
import random
import datetime
import string
import telepot
from telepot import flavor
import answerscan

from answerscan import genera_risposta

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print ('content_type: %s chat_type: %d chat_id: %s' % content_type, chat_type, chat_id)
    print(msg)
    msg_flavoror=flavor(msg)
    print('flavor: %s' % msg_flavoror)
    # Do your stuff according to `content_type` ...
    chat_id = msg['chat']['id']
    first_name = msg['from']['first_name']
    text = msg['text']
    #print ('first_name:' % first_name)
    #print('messaggio:' % text)
    #print ('Got command: %s' % text)

    messaggio = text.split(" ")
    for parola in messaggio:
        print (parola)
        text=parola

        if text in ['Ciao','ciao','bella','Bella*']:
            message = text + ' a te ' + first_name + '!'
            bot.sendMessage(chat_id, message)

        if text in ['facepalm','Facepalm','mapporch','chupa']:
            #message = text + ' a te ' + first_name + '!'
            #bot.sendMessage(chat_id, message)
            f = open('img/facepalm.jpg', 'rb')  # some file on local disk
            bot.sendPhoto(chat_id, f)

        if text in ['Perchè?','perchè?','perché?','Perché?','perchè']:
            answer_file=open('answers/why.answers', 'r')
            #message = genera_risposta(open('answers/why.answers', 'r'))
            message = genera_risposta(answer_file)
            bot.sendMessage(chat_id, message)

        if text.strip('!') in ['Stoca','StocaBot','stoca']:
            answer_file=open('answers/me.answers', 'r')
            #message = genera_risposta(open('answers/why.answers', 'r'))
            message = genera_risposta(answer_file)
            bot.sendMessage(chat_id, message)

        if text == '/tastiera':
            message = 'Ciao' + first_name + ', hai richiesto la tastiera'
            bot.sendMessage(chat_id, message)
            show_keyboard = {'keyboard': [['Lah Uno', 'Lah Duee'], ['o lah Thhreeh', 'Esci']]}
            bot.sendMessage(chat_id, 'This is a custom keyboard', reply_markup=show_keyboard)

        if text == '/mike':
            message = 'Allora signor ' + first_name + ', che busta sceglie?'
            show_keyboard = {'keyboard': [['Lah Uno', 'Lah Duee'], ['lah Thhreeh', 'Esci']]}
            bot.sendMessage(chat_id, message,reply_markup=show_keyboard)

        if text in 'Thhreeh':
            hide_keyboard = {'hide_keyboard': True}
            message = 'Allora signor ' + first_name + ', mi dica, come mai eh, se la mucca fa "muuuu" il merlo non fa "meee" ?'
            #bot.sendMessage(chat_id, message)
            bot.sendMessage(chat_id, message,reply_markup=hide_keyboard)

        if text == 'Esci':
            message = 'Lei ha scelto ' + text + ' quindi, se ne può anche adare a quel paese eh... Ma hai capito Mario Bianchi questi concorrenti eh?!!'
            hide_keyboard = {'hide_keyboard': True}
            bot.sendMessage(chat_id, message, reply_markup=hide_keyboard)

#TOKEN = sys.argv[1]  # get token from command-line
TOKEN='156945354:AAEWNo27Nq-VtPaFTCSslmrxln9w2MTLumg'
bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
#bot.sendMessage(chat_id_returned, 'Good morning!')
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)