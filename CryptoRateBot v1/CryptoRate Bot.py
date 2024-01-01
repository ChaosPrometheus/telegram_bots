import telebot
import requests
from bs4 import BeautifulSoup
bot = telebot.TeleBot('')

@ bot.message_handler(commands = ['start'])
def welcome(message):
     bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ бот показываюший курс криптавалютов,просто напиши ETH,BTC,BNB,Doge ."
                      .format(message.from_user, bot.get_me()))

@bot.message_handler(content_types=['text'])
def rate(message):
             headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
        #курс Эфириума
             url = 'https://ru.investing.com/crypto/ethereum'
             full_page = requests.get(url, headers=headers)
             soup = BeautifulSoup(full_page.content, 'html.parser')
             ethereum = soup.find("span",{"class": "pid-1061443-last", "id": "last_last"})

        #курс Биткоина
             url2 = 'https://ru.investing.com/crypto/bitcoin/btc-usd'
             full_page = requests.get(url2, headers=headers)
             soup2 = BeautifulSoup(full_page.content, 'html.parser')
             bitcoin = soup2.find("span",{"class": "text-2xl", "data-test": "instrument-price-last"})

        #курс Доги коина
             url3 = 'https://ru.investing.com/crypto/dogecoin/doge-usd'
             full_page = requests.get(url3, headers=headers)
             soup3 = BeautifulSoup(full_page.content, 'html.parser')
             doge = soup3.find("span",{"class": "text-2xl", "data-test": "instrument-price-last"})

        #курс BNB коина
             url4 = 'https://ru.investing.com/crypto/bnb/bnb-usd'
             full_page = requests.get(url4, headers=headers)
             soup4 = BeautifulSoup(full_page.content, 'html.parser')
             bnb = soup4.find("span",{"class": "text-2xl", "data-test": "instrument-price-last"})
                 
        #отправка данных
             if message.text == 'ETH':
                  bot.send_message(message.chat.id, 
                  "{0.first_name} Вот держите курс: 1 Эфириума  = "
                  .format(message.from_user, bot.get_me()) + ethereum.text + " доллара")
             if message.text == 'BTC':
                  bot.send_message(message.chat.id, 
                  "{0.first_name} Вот держите курс: 1 Биткоина  = "
                  .format(message.from_user, bot.get_me()) + bitcoin.text + " доллара")
             if message.text == 'Doge':
                  bot.send_message(message.chat.id, 
                  "{0.first_name} Вот держите курс: 1 Догикоина  = "
                  .format(message.from_user, bot.get_me()) + doge.text + " доллара")
             if message.text == 'BNB':
                  bot.send_message(message.chat.id, 
                  "{0.first_name} Вот держите курс: 1 BNB  = "
                  .format(message.from_user, bot.get_me()) + bnb.text + " доллара")

                  return rate      

bot.polling(none_stop=True)