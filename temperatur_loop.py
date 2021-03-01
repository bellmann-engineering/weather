import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    temperature_c = dhtDevice.temperature
    print("Die aktuelle Temperatur ist: {:.1f} C".format(temperature_c))

    time.sleep(2.0)


