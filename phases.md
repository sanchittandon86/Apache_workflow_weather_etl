Phase 0 
Goal
Create the project structure and install dependencies.
Deliverable: Empty project ready.
weather_etl/
│
├── app/
├── airflow/
│   └── dags/
├── data/
├── logs/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env

Phase 1
Fetch weather data from a public API.

Step 1
Below are commands to Create Virtual Environment 
[python3 -m venv venv]
[source venv/bin/activate]

Step 2
We'll only install what we need for this phase.
[pip install requests]

-----------

Phase 2
pip install pandas
create transform.py in App
structure the data in any format you like I did it like units and data is stored differently 

phase 3
convert the transformed data into csv
(venv) sanchittandon@VF396 weather_etl % cat data/weather.csv
time,temperature,temperature_unit,humidity,humidity_unit,wind_speed,wind_speed_unit
2026-07-01T14:15,26.0,°C,92,%,15.4,km/h

Phase 4
Step 1 — Install PostgreSQL Driver
[pip install psycopg2-binary]

Step 2 [Docker Setup]
docker compose up -d

Step 3 — Initialize Postgres
docker exec -it weather-to-postgres psql -U postgres

Step 4 — Create a Database
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP,
    temperature NUMERIC,
    humidity INTEGER,
    wind_speed NUMERIC
);

Load Data into PostgreSQL