import requests # pip3 install requests

city = "Wolfsburg"
token = "c417bfd432d32985a579e4363b63a49f"
url_weathermap = f"http://api.openweathermap.org/data/2.5/weather?q={city},de&APPID={token}&units=metric"
# print(url_weathermap)


resp_outdoor = requests.get(url_weathermap)

if resp_outdoor.status_code != 200: # ok
    raise Exception("GET auf openweathermap war nicht erfolgreich")

outdoor_temperatur = resp_outdoor.json()["main"]["temp"]

print(f"Outdoor: {outdoor_temperatur} °C") 

