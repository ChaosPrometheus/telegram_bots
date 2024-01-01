import telebot
from telebot import types
    # Создаешь бота в телеграме и там будет токен и его вставишь вот сюда
    # Не забудь до и после вставить скобки 
bot = telebot.TeleBot("#твой токен")
 
@bot.message_handler(commands=['start'])
def welcome(message):
    # Это тебе передает стикер ,где стоит файл кода
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
   
    # Это клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    item4 = types.KeyboardButton("4")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?", reply_markup=markup)
    # ответы на клавиатуру
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == '1':
        bot.send_message(message.chat.id, "твои надписи")
    if message.text == '2':
        bot.send_message(message.chat.id, "твои надписи,")
    if message.text == '3':
        bot.send_message(message.chat.id, "твои надписи.")
    if message.text == '4':
        bot.send_message(message.chat.id, "твои надписи,.")
    # Запуск
bot.polling(none_stop=True)
