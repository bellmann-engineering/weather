from Adafruit_IO import Client # pip3 install adafruit-io

ADAFRUIT_IO_USERNAME = 'kbellmann' # CHANGE IT!!!
ADAFRUIT_IO_KEY = 'aio_qGNO30nLu9XyR705k1CqqqAoxhtW' # CHANGE IT!!!

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

feed_key = "temperatur"

temp_c = aio.receive(feed_key)

print(temp_c.value)