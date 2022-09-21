from Adafruit_IO import Client # pip3 install adafruit-io

ADAFRUIT_IO_USERNAME = 'kbellmann'
ADAFRUIT_IO_KEY = 'aio_Glyp88O8yi6f0uv4nKWx4iH3sOX2'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

current_temp = aio.receive('temperatur').value

print(f"Die Temperatur beträgt {current_temp} °C")
