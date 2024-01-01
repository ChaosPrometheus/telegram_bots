import telebot

bot = telebot.TeleBot('')

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    id_channel_1 = '' 
    id_channel_2 = ''
    bot.forward_message(id_channel_2, id_channel_1, message.message_id)

bot.polling()
