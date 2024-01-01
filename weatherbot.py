from pyowm import OWM
from pyowm.utils import config, timestamps
from pyowm.utils.config import get_default_config
import telebot
#API
bot = telebot.TeleBot("")
owm = OWM('')
#Язык
config_dict = get_default_config()
config_dict['language'] = 'ru'
#Приветсвие
@ bot.message_handler(commands = ['start'])
def welcome(message):
    bot.send_message( message.from_user.id , "Привет, я бот показываюший информация о погоде в городах,просто напиши свой город")
    
#запрос города или села
@bot.message_handler(content_types=['text'])
def weather(message):
        try:
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text) 
            w = observation.weather
            status = w.detailed_status  #статус облока
            wind = w.wind()["speed"]  #скорость ветра
            humidity = w.humidity  #влажность
            temp = w.temperature('celsius')["temp"]  #температура
            answer = "В этом Городе/селе " + message.text + " сейчас " + status + ".\n"
            answer += "Температура " + str(temp) + " градуса.\n"
            answer += "Скорость Ветра " + str(wind) + " м/с.\n"
            answer += "Влажность " + str(humidity) + "%.\n"
        except:
            answer = "Данный город не найден"
        finally:
            bot.send_message(message.chat.id , answer)
    
            return weather

bot.polling()
