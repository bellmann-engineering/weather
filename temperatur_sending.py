from Adafruit_IO import Client # pip3 install adafruit-io

ADAFRUIT_IO_USERNAME = 'kbellmann'
ADAFRUIT_IO_KEY = ''

io = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

feed = "temperatur"

temp_c = "24"

io.send_data(feed, temp_c)



