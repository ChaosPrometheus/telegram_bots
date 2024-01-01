from aiogram import Bot, Dispatcher, executor, types
from pyowm import OWM
from pyowm.utils import config,timestamps
from pyowm.utils.config import get_default_config

#API
TOKEN = ""
owm = OWM('')

#Язык
config_dict = get_default_config()
config_dict['language'] = 'ru'

#Функции бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#команда на запуск
@dp.message_handler(commands=['start'])
async def main(message: types.Message):
        await bot.send_message(message.from_user.id, "Привет, я бот показываюший информация о погоде в городах или селах,просто напиши свое местоположение")

#отправка данных
@dp.message_handler(content_types=['text'])
async def weather(message: types.Message):
        try:
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text) 
            w = observation.weather
            status = w.detailed_status  #статус облока
            wind = w.wind()["speed"]  #скорость ветра
            humidity = w.humidity  #влажность
            temp = w.temperature('celsius')["temp"]  #температура
            print(message.text,"температура:",temp)
            answer = ("В этом Городе/селе " + message.text + ".\n"
            + "Сейчас " + status + ".\n"
            + "Температура " + str(temp) + " градуса.\n"
            + "Скорость Ветра " + str(wind) + " м/с.\n"
            + "Влажность " + str(humidity) + "%.\n")
        except:
            answer = "Данный город не найден"
        finally:
                await bot.send_message(message.from_user.id, answer)

                return weather

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
