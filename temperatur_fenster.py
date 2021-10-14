import requests # python -m pip install requests
import json
import time
from tkinter import *

url = "https://io.adafruit.com/api/v2/kbellmann/feeds/temperatur/data"

fenster = Tk()
fenster.geometry("400x400")
fenster.option_add('*Font', '19')

lbox = Listbox(fenster)
lbox.pack(side="left",fill="both", expand=True)

exit_button = Button(fenster, text="Schliessen", command=fenster.quit)
exit_button.pack(side="bottom", pady=20)

resp = requests.get(url)

if resp.status_code != 200:
    raise ApiError('GET /temperatur/ {}'.format(resp.status_code))

for item in resp.json():
    epoch = item["created_epoch"]
    temperatur = item["value"]
    when = time.strftime('%H:%M:%S (%d.%m)', time.localtime(epoch))
    # print("{} - {} °C".format(when , temperatur))
    lbox.insert("end", "{} - {} °C".format(when , temperatur))
	
	
fenster.mainloop()
