#Настройки
import telebot

URL = 'https://banki24.by/minsk/kurs/usd'
TOKEN = '991563317:AAF8ydELcbOWHNCgWDzdRzFqzq-KFhq7-Xw'

BOT = telebot.TeleBot(TOKEN)

BUTTON_GET_ALL_LIST = 'Список банков и валют'
BUTTON_GET_BEST_BUY_PRICE = 'Лучший курс по покупке'
BUTTON_GET_BEST_SELL_PRICE = 'Лучший курс по продаже'
BUTTON_START = 'Вернуться в начало'

BUTTON_USD = 'USD'

def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard

KEYBOARD_CHOICE = create_keyboard()
KEYBOARD_CHOICE.row(BUTTON_GET_ALL_LIST)
KEYBOARD_CHOICE.row(BUTTON_GET_BEST_BUY_PRICE, BUTTON_GET_BEST_SELL_PRICE)
KEYBOARD_CHOICE.row(BUTTON_START)
