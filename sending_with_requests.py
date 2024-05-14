import requests
import json

username = "your_username"
key = "your_key"
feed_name = "your_feed_name"
data = {
    "value": 25
}

url = f"https://io.adafruit.com/api/v2/{username}/feeds/{feed_name}/data"
headers = {
    "Content-Type": "application/json",
    "X-AIO-Key": key
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Data sent successfully.")
else:
    print(f"Failed to send data. Status code: {response.status_code}")
