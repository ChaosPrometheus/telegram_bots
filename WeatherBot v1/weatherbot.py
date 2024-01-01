from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import telebot
bot = telebot.TeleBot("")
owm = OWM('')

config_dict = get_default_config()
config_dict['language'] = 'ru'

@ bot.message_handler(commands = ['start'])
def welcome(message):
    bot.send_message( message.from_user.id , "Привет, я бот показываюший информация о погоде в городах,просто напиши свой город")

@bot.message_handler(content_types=['text'])
def weather(message):
        try:
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text) 
            w = observation.weather
            temp = w.temperature('celsius')["temp"]
            wind = w.wind()["speed"]
            humidity = w.humidity
            clouds = w.detailed_status
            answer = "В городе " + message.text + " сейчас " + clouds + ".\n"
            answer += "Температура " + str(temp) + " градуса\n"
            answer += "Скорость Ветра " + str(wind) + " м/с," + " Влажность " + str(humidity) + "%\n"
        except:
            answer = "Данный город не найден"
        finally:
                bot.send_message( message.chat.id , answer)
            
                return weather
bot.polling()
