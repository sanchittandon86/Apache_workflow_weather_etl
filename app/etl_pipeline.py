from extract import fetch_weather
from transform import transform_weather
from load import load_to_postgres, save_to_csv
from logger import logger


def run_pipeline():

    logger.info("Starting ETL Pipeline")

    weather = fetch_weather()

    logger.info("Weather fetched successfully")

    df = transform_weather(weather)

    logger.info("Data transformed successfully")

    save_to_csv(df)

    logger.info("CSV generated")

    load_to_postgres(df)

    logger.info("Data loaded into PostgreSQL")

    logger.info("Pipeline completed successfully")



if __name__ == "__main__":
    run_pipeline()