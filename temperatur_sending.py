import time
from Adafruit_IO import Client, Feed, RequestError # pip install adafruit-io

ADAFRUIT_IO_USERNAME = 'kbellmann'
ADAFRUIT_IO_KEY = ''

io = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#feed = io.feeds('temperatur')

feed = "temperatur"

temp = "23"

#io.send(feed, temp)


metadata = {'lat': 49.460983,
            'lon': 11.061859,
            'ele': 300,
            'created_at': None}
io.send_data(feed, temp, metadata)

