import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4)

temperature_c = dhtDevice.temperature
temperature_f = temperature_c * (9 / 5) + 32
print("Die aktuelle Temperatur ist: {:.1f} F / {:.1f} C".format(temperature_f, temperature_c))
