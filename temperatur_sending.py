import time
from Adafruit_IO import Client # pip3 install adafruit-io

ADAFRUIT_IO_USERNAME = 'kbellmann'
ADAFRUIT_IO_KEY = ''

io = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

feed = "temperatur"

temp = "24"

#metadata = {'lat': 49.460983,
#            'lon': 11.061859,
#            'ele': 300,
#            'created_at': None}
# io.send_data(feed, temp, metadata)
io.send_data(feed, temp_c)

