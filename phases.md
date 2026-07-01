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