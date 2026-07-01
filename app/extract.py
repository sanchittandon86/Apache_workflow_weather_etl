import requests

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

response = requests.get(API_URL)

print(response.status_code)

data = response.json()

print(data)
