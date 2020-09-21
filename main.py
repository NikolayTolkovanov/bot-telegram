#Здесь выполняются все действия

from settings.SETTINGS import *
from parse.parse import Parse
from parse.dataPy import Data


parse = Parse(URL).get_content()
data = Data(parse)




@BOT.message_handler(commands=['start'])
def start_message(message):   
    BOT.send_message(message.chat.id, 'Выберите валюту...', reply_markup=create_keyboard().row('USD'))

@BOT.message_handler(content_types=['text'])
def get_message(message):
    
    if message.text == BUTTON_USD:

        BOT.send_message(message.chat.id, 'Приветули! Что вы хотите сделать?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_ALL_LIST: 
         BOT.send_message(message.chat.id, data.get_all_list(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_BEST_BUY_PRICE: 
         BOT.send_message(message.chat.id, data.get_best_buy_price(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_BEST_SELL_PRICE: 
         BOT.send_message(message.chat.id, data.get_best_sell_price(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_START:
        start_message(message)

    else:
        BOT.send_message(message.chat.id, 'Я не понимаю вас, напишите хотя-бы "/start" из приличия...')



BOT.polling()


