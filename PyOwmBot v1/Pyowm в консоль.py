from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('')
def weather():
    try:
        mgr = owm.weather_manager()
        city = input('город ')
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        wind = w.wind()["speed"]
        humidity = w.humidity
        status = w.detailed_status
        print("В городе " + city + " сейчас " + str(status) + ".")
        print("Температура " + str(temp) + " градуса.")
        print("Скорость Ветра " + str(wind) + " м/с,")
        print("Влажность " + str(humidity) + "%")
    except:
        print(city + " город не найден")
    weather()
weather()

               
                
            
        
      

