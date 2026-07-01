from extract import fetch_weather
from transform import transform_weather
from database import get_connection


def save_to_csv(df, filename="data/weather.csv"):
    """
    Save the DataFrame to a CSV file.
    """
    df.to_csv(filename, index=False)
    print(f"CSV saved successfully at {filename}")


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

    print("Data loaded into PostgreSQL successfully!")


if __name__ == "__main__":
    weather = fetch_weather()
    df = transform_weather(weather)

    save_to_csv(df)
    load_to_postgres(df)