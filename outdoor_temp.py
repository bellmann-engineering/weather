import requests # pip3 install requests
import time

city = "Wolfsburg"
token = "c417bfd432d32985a579e4363b63a49f"
url_weathermap = "http://api.openweathermap.org/data/2.5/weather?q={},de&APPID={}&units=metric".format(city , token)

resp_outdoor = requests.get(url_weathermap)

if resp_outdoor.status_code != 200: # ok
    raise Exception("GET auf openweathermap war nicht erfolgreich")

outdoor_temperatur = resp_outdoor.json()["main"]["temp"]
outdoor_epoch = resp_outdoor.json()["dt"]
lesbare_uhrzeit = time.strftime("%H:%M:%S [%d.%m.%Y]", time.localtime(outdoor_epoch))
print("Outdoor: {} - {} °C".format(lesbare_uhrzeit, outdoor_temperatur)) 

