import pandas as pd
from logger import logger


def transform_weather(weather_json):
    """
    Transforms the weather API JSON response into a pandas DataFrame.
    """

    logger.info("Transforming weather data...")

    current = weather_json["current"]

    record = {
        "time": current["time"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
    }

    df = pd.DataFrame([record])

    logger.info("Transformation completed successfully.")

    return df


if __name__ == "__main__":
    from extract import fetch_weather

    weather = fetch_weather()
    df = transform_weather(weather)

    logger.info(df)