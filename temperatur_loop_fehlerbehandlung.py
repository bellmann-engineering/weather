import board
import adafruit_dht
import time
 
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

while True:
  try:
    temperature_c = dhtDevice.temperature
    print("Die aktuelle Temperatur ist: {:.1f} C".format(temperature_c))
    
   except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
        
    time.sleep(2)
    
