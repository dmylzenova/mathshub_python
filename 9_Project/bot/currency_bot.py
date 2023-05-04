import re
import requests

import logging
import telebot
from telebot import types
from bs4 import BeautifulSoup

# добавим логгирование, чтобы получать сообщения в консоль
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

def run_currency_bot(token: str) -> None:
    """ Run bot that return today currency from https://cbr.ru/"""
    bot = telebot.TeleBot(token, parse_mode=None)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        """ Respond to text messages"""
        if message.text == "/start":

            keyboard = types.InlineKeyboardMarkup()
            key_usd = types.InlineKeyboardButton(text='Доллар', callback_data='usd')
            keyboard.add(key_usd)
            key_eur = types.InlineKeyboardButton(text='Евро', callback_data='eur')
            keyboard.add(key_eur)
            key_cny = types.InlineKeyboardButton(text='Юань', callback_data='cny')
            keyboard.add(key_cny)
            bot.send_message(message.from_user.id,
                             "Привет! Я бот-конвертер валют.\nВведите валюту для которой вы хотите получить её курс ЦБ.",
                             reply_markup=keyboard)
        elif message.text == "":
            bot.send_message(message.from_user.id, "Введите валюту для которой вы хотите получить её курс ЦБ")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        """ Respond to keyboard calls"""
        if call.data not in ('usd', 'eur', 'cny'):
            bot.send_message(call.message.chat.id, 'Я пока не умею работать с этой валютой')

        r = requests.get('https://cbr.ru/')
        soup = BeautifulSoup(r.text, "html.parser")
        data = soup.findAll('div', class_='col-md-2 col-xs-9 _right mono-num')

        if len(data) != 6:
            bot.send_message(call.message.chat.id, 'Упссс я сломался')

        helper = {'usd': [0, "доллара"], 'eur': [2, "евро"], 'cny': [4, "юаня"]}[call.data]
        info = str(data[helper[0]])

        value = float(re.search(r'(\d+,?\d*)\s*₽', info).group(1).replace(',', '.'))
        bot.send_message(call.message.chat.id, f'Текущий курс {helper[1]} равен {value} рублей')

    # запустим бота
    bot.infinity_polling()
