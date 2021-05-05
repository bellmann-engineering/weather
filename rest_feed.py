import requests # python -m pip install requests
import json
import time

url = "https://io.adafruit.com/api/v2/JanBoltz/feeds/tempdah/data"

resp = requests.get(url)

if resp.status_code != 200:
    # nicht ok
    raise ApiError('GET /airports/ {}'.format(resp.status_code))

for item in resp.json():
    epoch = item["created_epoch"]
    temperatur = item["value"]
    when = time.strftime('%H:%M:%S (%d.%m)', time.localtime(epoch))
    print("{} - {} °C".format(when , temperatur))
