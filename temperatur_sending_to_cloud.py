from Adafruit_IO import Client # pip3 install adafruit-io

ADAFRUIT_IO_USERNAME = 'kbellmann' # CHANGE IT!!!
ADAFRUIT_IO_KEY = 'aio_oBqP91rlunrtx5jXprpbpt0KLmbo' # CHANGE IT!!!

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#feed = io.feeds('temperatur')

feed = "temperatur"

temp_c = "23"

aio.send_data(feed, temp_c)


