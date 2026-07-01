import requests

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

def fetch_weather():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        print("API Success: ", response.status_code)
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"API Failed: {e}")

if __name__ == "__main__":
    weather = fetch_weather()
    print(f"Time: {weather['current']['time']}")
    print(f"Temperature: {weather['current']['temperature_2m']} {weather['current_units']['temperature_2m']}")
    print(f"Humidity: {weather['current']['relative_humidity_2m']} {weather['current_units']['relative_humidity_2m']}")
    print(f"Wind Speed: {weather['current']['wind_speed_10m']} {weather['current_units']['wind_speed_10m']}")