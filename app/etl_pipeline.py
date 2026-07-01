from extract import fetch_weather
from transform import transform_weather
from load import load_to_postgres, save_to_csv


def run_pipeline():

    print("Starting ETL Pipeline...")

    weather = fetch_weather()

    df = transform_weather(weather)

    save_to_csv(df)

    load_to_postgres(df)

    print("Pipeline Completed Successfully!")


if __name__ == "__main__":
    run_pipeline()