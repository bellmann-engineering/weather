import sys
import time
import board
import adafruit_dht

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
YELLOW= "\033[0;33m" 
RESET = "\033[0;0m"

try:
    count = int(sys.argv[1])
except:
    print ("Bitte geben Sie die Anzahl der duchzuführenden Messungen ein: ")
    count = int(input())

print()
try:
    limit = float(sys.argv[2])
except:
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
        print("Die aktuelle Luftfeuchtigkeit ist: ", dhtDevice.humidity)

        if temperature_c > max:
            max = temperature_c
        
        if temperature_c < min:
            min = temperature_c

        if temperature_c > limit:
            sys.stdout.write(RED)
            print("Schwellenwert überschritten: " , limit)
            sys.stdout.write(RESET)
        i += 1
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0) # im Fehlerfall noch einmal 2s warten
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)

dhtDevice.exit()
print()

sys.stdout.write(BLUE)
print("Die niedrigste Tagestemperatur: " , min)

sys.stdout.write(YELLOW)
print("Die höchste Tagestemperatur: " , max)

print()

sys.stdout.write(RESET)
print("Ende Messung")
print()
