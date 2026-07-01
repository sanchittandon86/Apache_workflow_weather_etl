import pandas as pd
from extract import fetch_weather

def transform_weather(weather_json):
    
    record = {
    "time": weather_json["current"]["time"],
    "temperature": weather_json["current"]["temperature_2m"],
    "temperature_unit": weather_json["current_units"]["temperature_2m"],
    "humidity": weather_json["current"]["relative_humidity_2m"],
    "humidity_unit": weather_json["current_units"]["relative_humidity_2m"],
    "wind_speed": weather_json["current"]["wind_speed_10m"],
    "wind_speed_unit": weather_json["current_units"]["wind_speed_10m"],
}

    df = pd.DataFrame([record])

    return df

if __name__ == "__main__":
    weather = fetch_weather()
    df = transform_weather(weather)

    print(df)