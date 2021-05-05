import requests # python -m pip install requests
import json

# List all airports or one specific airport. 
# All airports response is very large. 

url = "https://api.lufthansa.com/v1/references/airports/FRA?lang=DE"
token = "tj5rvwrewxqpqptv7uetv266"

resp = requests.get(url,
      headers={'Content-Type':'application/json',
               'Authorization': 'Bearer {}'.format(token)})

if resp.status_code != 200:
    # nicht ok
    raise ApiError('GET /airports/ {}'.format(resp.status_code))

print(resp.json()["AirportResource"]["Airports"]["Airport"]["Position"])
