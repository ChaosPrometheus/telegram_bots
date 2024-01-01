import serial
import telebot
from telebot import types
ser = serial.Serial(port = "COM3")  
ser.reset_input_buffer()

bot = telebot.TeleBot("5244333565:AAF6uyXxLwBMzpX3aF-rGI9lysB-rIDtsDo")

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("0")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "1":
        bot.send_message(message.chat.id, "Вкл")
        ser.write(b'H')
                
    if message.text == "0":
        ser.write(b'L')
        bot.send_message(message.chat.id, "Выкл")
bot.polling(none_stop=True)
