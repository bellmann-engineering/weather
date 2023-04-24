# Beachte: der Sensor kann nur alle 2s abgefragt werden!

import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

temperature_c = dhtDevice.temperature
print("Die aktuelle Temperatur ist: {:.1f} C".format(temperature_c))
