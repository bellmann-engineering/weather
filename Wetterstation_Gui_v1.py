from tkinter import *

#pip install Pillow
#linux: sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk, Image

#Bzgl. der Webbilder
import urllib.request as urllib2
from io import BytesIO

import time

# Ein einfaches Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Hallo Wolfsburg")

#WetterIcon aus dem Web
path = ("http://openweathermap.org/img/wn/02n@4x.png")
webimg = urllib2.urlopen(path)
raw_data = webimg.read()
webimg.close()
img = ImageTk.PhotoImage(Image.open(BytesIO(raw_data)))

panel = Label(fenster, image = img)
panel["background"]="lightgreen"
panel.pack(side = "bottom", fill = "both", expand = "yes")

# Uhrzeit wird über ein Label angezeigt und mit pack im fenster gezeigt
uhr = Label(master=fenster,
            font=('Arial',30),
            fg='blue',
            width = 15,
            height = 3)
uhr.pack()

zeit = ''
def tick(  ):
    global zeit
    neuezeit = time.strftime('%H:%M:%S')
    if neuezeit != zeit:
        zeit = neuezeit
        uhr.config(text = zeit) 
    uhr.after(200, tick) 
 
tick()
# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()
