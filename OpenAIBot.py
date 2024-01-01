import openai
import telebot

bot = telebot.TeleBot("5941862271:AAHrXG2BYJXyDmYaXefVpFxDdsQvCqnVI9I")
openai.api_key = "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"

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(message.chat.id,"Привет, я бот с Искуственным Интелектом")

@bot.message_handler(content_types=['text'])
def hello(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
)
  bot.send_message(message.chat.id, response['choices'][0]['text'])

bot.polling()
