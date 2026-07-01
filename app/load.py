from extract import fetch_weather
from transform import transform_weather
from database import get_connection
from logger import logger
import os


def save_to_csv(df):
    output_dir = os.getenv("DATA_DIR", "data")

    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.join(output_dir, "weather.csv")

    df.to_csv(filename, index=False)

    logger.info(f"CSV saved successfully at {filename}")


def load_to_postgres(df):
    """
    Load the DataFrame into PostgreSQL.
    """
    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO weather_data
            (time, temperature, humidity, wind_speed)
            VALUES (%s, %s, %s, %s)
            """,
            (
                row["time"],
                row["temperature"],
                row["humidity"],
                row["wind_speed"],
            ),
        )

    conn.commit()

    cursor.close()
    conn.close()

    logger.info("Data loaded into PostgreSQL successfully!")


if __name__ == "__main__":
    weather = fetch_weather()
    df = transform_weather(weather)

    save_to_csv(df)
    load_to_postgres(df)