# -*- coding: utf-8 -*-
import requests, datetime
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from translate import Translator

a = str(datetime.datetime.now())
l = list(a)
real_date = l[8]+ l[9]+"."+l[5]+l[6]+"."+l[0]+l[1]+l[2]+l[3]

url_exchange_rate = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='+str(real_date)

response_1 = json.loads(requests.get(url_exchange_rate).text)
date = response_1.get('date')
#currency_eur = response_1.get('exchangeRate')[22].get('purchaseRate')
sale_eur = response_1.get('exchangeRate')[22].get('saleRate')
purchase_eur = response_1.get('exchangeRate')[22].get('purchaseRate')
#currency_usd = response_1.get('exchangeRate')[16].get('purchaseRate')
sale_usd = response_1.get('exchangeRate')[16].get('saleRate')
purchase_usd = response_1.get('exchangeRate')[16].get('purchaseRate')
#currency_rub = response_1.get('exchangeRate')[14].get('purchaseRate')
sale_rub = response_1.get('exchangeRate')[14].get('saleRate')
purchase_rub = response_1.get('exchangeRate')[14].get('purchaseRate')

result_currency = "На дату " + str(date) + " курс ПриватБанка:" + "\n" + \
                  "EUR " + "курс покупки = " + str(purchase_eur) + " UAH; курс продажи = " + str(sale_eur) + " UAH;" \
        "" + "\n" + "USD " + "курс покупки = " + str(purchase_usd) + " UAH; курс продажи = " + str(sale_usd) + " UAH;" \
   "\n" + "RUB" + " курс покупки = " + str(purchase_rub) + " UAH; курс продажи = " + str(sale_rub) + " UAH;"
token = '779076598:AAFkrGDOrc6LNJkIat3aDxFXTkkAsLho620'

updater = Updater(token=token)
dispatcher = updater.dispatcher

def textTranslator(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="я постараюсь помочь перевечти, с русского на английский "
                                                          "что тебе нужно, вводи свой текст \n")
    translator = Translator(from_lang="russian", to_lang="english")
    translation = translator.translate(args[0])
    bot.send_message(chat_id=update.message.chat_id, text=translation)

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello I am @Kraken_hero_bot ')

def textMessage(bot, update):
    if "курс валют" in update.message.text.lower():
        response = (result_currency)
        bot.send_message(chat_id=update.message.chat_id, text=response)
    if "переводчик" in update.message.text.lower():
        textTranslator(bot, update)

    else:
        response_2 = 'Get your message: ' + update.message.text
        bot.send_message(chat_id=update.message.chat_id, text=response_2)

start_command_handler = CommandHandler('start', startCommand)
translate_command_handler = CommandHandler('translate', textTranslator, pass_args=True)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(translate_command_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()

