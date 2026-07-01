from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

import sys
import os

# Add app folder to Python path
sys.path.append("/opt/airflow/app")

from etl_pipeline import run_pipeline


default_args = {
    "owner": "sanchit",
    "retries": 1,
}


with DAG(
    dag_id="weather_etl_pipeline",
    default_args=default_args,
    description="Weather ETL Pipeline",
    start_date=datetime(2026, 7, 1),
     schedule="* * * * *",
    catchup=False,
    tags=["etl", "weather"],
) as dag:

    weather_etl = PythonOperator(
        task_id="run_weather_etl",
        python_callable=run_pipeline,
    )