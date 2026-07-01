import requests
from logger import logger
from config import API_URL

def fetch_weather():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        logger.info("API Success: %s", response.status_code)
        return response.json()
    except requests.RequestException as e:
        logger.error("API Failed: %s", e)
        raise Exception(f"API Failed: {e}")

if __name__ == "__main__":
    weather = fetch_weather()
    logger.info("Time: %s", weather['current']['time'])
    logger.info("Temperature: %s %s", weather['current']['temperature_2m'], weather['current_units']['temperature_2m'])
    logger.info("Humidity: %s %s", weather['current']['relative_humidity_2m'], weather['current_units']['relative_humidity_2m'])
    logger.info("Wind Speed: %s %s", weather['current']['wind_speed_10m'], weather['current_units']['wind_speed_10m'])