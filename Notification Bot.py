import telebot
from plyer import notification

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "просто напиши сообщение для компьютера")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    notification.notify(
        title="Новое сообщение",
        message=message.text,
        timeout=10  
    )

bot.polling()
