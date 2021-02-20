import board
import adafruit_dht
import time
 
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

while True:
  temperature_c = dhtDevice.temperature
  print("Die aktuelle Temperatur ist: {:.1f} C".format(temperature_c))
  
  time.sleep(2)
