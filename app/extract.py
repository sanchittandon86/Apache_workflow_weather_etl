import requests
from config import API_URL
from logger import logger


def fetch_weather():
    try:
        logger.info("Fetching weather data from API...")

        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        logger.info("Weather data fetched successfully.")

        return response.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
        raise


if __name__ == "__main__":
    weather = fetch_weather()

    current = weather["current"]

    logger.info(f"Time: {current['time']}")
    logger.info(f"Temperature: {current['temperature_2m']}°C")
    logger.info(f"Humidity: {current['relative_humidity_2m']}%")
    logger.info(f"Wind Speed: {current['wind_speed_10m']} km/h")