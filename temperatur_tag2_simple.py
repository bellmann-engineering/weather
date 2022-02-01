import time
import board
import adafruit_dht

print ("Bitte geben Sie die Anzahl der duchzuführenden Messungen ein: ")
count = int(input())

print()

print ("Bitte geben Sie den Schwellenwert für die Temperatur ein: ")
limit = float(input())

print()

dhtDevice = adafruit_dht.DHT22(board.D4)
min = 999
max = 0

print("Starte Messungen: ")

i = 0
while i < count:
    try:
        temperature_c = dhtDevice.temperature
        print("Die aktuelle Temperatur ist: {:.1f} C".format(temperature_c)) 

        if temperature_c > max:
            max = temperature_c
        
        if temperature_c < min:
            min = temperature_c

        if temperature_c > limit:
            print("Schwellenwert überschritten: " , limit)
        i += 1
    except RuntimeError as error:
        time.sleep(2.0) # im Fehlerfall noch einmal 2s warten
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)

dhtDevice.exit()
print()

print("Die niedrigste Tagestemperatur: " , min)
print("Die höchste Tagestemperatur: " , max)
