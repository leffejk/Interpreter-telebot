import telebot
import Yandex_translate_offers
import Yandex_translate_words
from alphabet import alphabet
from info import info

def language_definition(text):
    ''' Используется для определения языка (по первой букве) '''
    if (text[0] > "a" and text[0] < "z") or (text[0] > "A" and text[0] < "Z"):
        return "en-ru"
    elif (text[0] > "а" and text[0] < "я") or (text[0] > "А" and text[0] < "Я"):
        return "ru-en"


TOKKEN = r"724744496:AAH08g3E2oA5MThJV8iP9fMCI7L9W0VQDa4"
BOT = telebot.TeleBot(TOKKEN)


@BOT.message_handler(commands=['start'])
def start_message(message):
    ''' Обработчик команды /start '''
    BOT.send_message(message.chat.id, 'Привет :) Это бот переводчик\nДля получения информации об использовании бота - введи /info')

@BOT.message_handler(commands=['alp'])
def start_message(message):
    ''' Обработчик команды /alp '''
    BOT.send_message(message.chat.id, alphabet())

@BOT.message_handler(commands=['info'])
def start_message(message):
    ''' Обработчик команды /info '''
    BOT.send_message(message.chat.id, info(),
                             parse_mode="HTML")

@BOT.message_handler(content_types=['text'])
def send_text(message):
    ''' Обработчик сообщений с текстом '''
    # if message.text == 'Привет':
    #     BOT.send_message(message.chat.id, 'Привет, мой создатель')
    try:
        if len(message.text.split()) > 1: # Если больше одно слова, запускать Yandex_translate_offers
            BOT.send_message(message.chat.id, Yandex_translate_offers.translate_offers(message.text,
                                                               language_definition(message.text)),
                             parse_mode="HTML", reply_to_message_id=message.message_id )
        elif len(message.text.split()) == 1: # Если одно слово, запускать Yandex_translate_words
            BOT.send_message(message.chat.id, Yandex_translate_words.main_functioin(message.text,
                                                                                    language_definition(message.text)),
                             parse_mode="HTML", reply_to_message_id=message.message_id )
    except:
        BOT.send_message(message.chat.id, "❌ Ошибка перевода.\n Бот строго относится к грамматике. Проверь, написал ли ты без ошибок? \n Или просто попробуй заменить слово на синоним.")
print("Start")

BOT.polling() # Не завершать работу бота