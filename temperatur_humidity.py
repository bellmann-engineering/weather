import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Aktuelle Temperatur: {:.1f} F / {:.1f} C\tLuftfeuchtigkeit: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0) # im Fehlerfall noch einmal 2s warten
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)


