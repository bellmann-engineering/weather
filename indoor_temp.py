from Adafruit_IO import Client # pip3 install adafruit-io

ADAFRUIT_IO_USERNAME = '<YOUR NAME>'
ADAFRUIT_IO_KEY = '<YOUR KEY>'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

current_temp = aio.receive('temperatur').value

print(f"Die Temperatur beträgt {current_temp} °C")
