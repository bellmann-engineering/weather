import requests # python -m pip install requests
import time

# pfad zum feed
url = "https://io.adafruit.com/api/v2/kbellmann/feeds/temperatur"

city = "Wolfsburg"
token = "c417bfd432d32985a579e4363b63a49f"
url_weathermap = "http://api.openweathermap.org/data/2.5/weather?q={},de&APPID={}&units=metric".format(city , token)

resp = requests.get(url)

resp_outdoor = requests.get(url_weathermap)

if resp.status_code != 200: # ok
    raise Exception("GET auf io.adafruit war nicht erfolgreich")

if resp_outdoor.status_code != 200: # ok
    raise Exception("GET auf openweathermap war nicht erfolgreich")

outdoor_temperatur = resp_outdoor.json()["main"]["temp"]
outdoor_epoch = resp_outdoor.json()["dt"]
lesbare_uhrzeit = time.strftime("%H:%M:%S [%d.%m.%Y]", time.localtime(outdoor_epoch))
print("Outdoor: {} - {} °C".format(lesbare_uhrzeit, outdoor_temperatur)) 
print()

raw = resp.json()
for r in raw:
    temperatur = r["value"]
    sekunden = r["created_epoch"]

    # umwandeln unix timestamp in lesbares datum
    # 06.05.2021 - 1.1.1970 = sekunden
    lesbare_uhrzeit = time.strftime("%H:%M:%S [%d.%m.%Y]", time.localtime(sekunden))

    print("Indoor: {} - {} °C".format(lesbare_uhrzeit, temperatur)) 
    break   


