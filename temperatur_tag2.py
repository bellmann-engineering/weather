import time
import board
import adafruit_dht

# Anzahl Messungen einlesen
while True:
    try:
        count = int(input("Bitte geben Sie die Anzahl der durchzuführenden Messungen ein: "))
        break
    except ValueError:
        print("Bitte eine gültige Ganzzahl eingeben.")

# Schwellenwerte einlesen und prüfen
while True:
    try:
        lower_limit = float(input("Bitte geben Sie die untere Temperaturschwelle ein: "))
        upper_limit = float(input("Bitte geben Sie die obere Temperaturschwelle ein: "))
        if upper_limit > lower_limit:
            break
        else:
            print("Die obere Schwelle muss größer als die untere Schwelle sein. Bitte erneut eingeben.")
    except ValueError:
        print("Bitte gültige Zahlen eingeben.")

print()

# Sensor vorbereiten
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
min_temp = 999
max_temp = -999

print("Starte Messungen: ")

i = 0
while i < count:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        print(f"Die aktuelle Temperatur ist: {temperature_c:.2f} °C")
        print(f"Die aktuelle Luftfeuchtigkeit ist: {humidity:.2f} %")

        if temperature_c > max_temp:
            max_temp = temperature_c
        
        if temperature_c < min_temp:
            min_temp = temperature_c

        # Schwellenwertprüfung mit if / elif / else
        if temperature_c > upper_limit:
            print(f"Temperatur über oberer Schwelle ({upper_limit:.2f} °C)!")
        elif temperature_c < lower_limit:
            print(f"Temperatur unter unterer Schwelle ({lower_limit:.2f} °C)!")
        else:
            print(f"Temperatur innerhalb der Grenzen {lower_limit:.2f} - {upper_limit:.2f} °C.")

        i += 1
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)  # im Fehlerfall noch einmal 2s warten
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)

dhtDevice.exit()
print()
print(f"Die niedrigste Tagestemperatur: {min_temp:.2f} °C")
print(f"Die höchste Tagestemperatur: {max_temp:.2f} °C")
print()
print("Ende Messung")
print()
