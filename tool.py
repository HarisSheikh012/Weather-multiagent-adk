import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv("./.env")

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city: str) -> dict:
    """Fetches real-time weather data for a given city using OpenWeatherMap API."""
    print(f"--- Tool: get_weather called for city: {city} ---")

    if not OPENWEATHER_API_KEY:
        return {
            "status": "error",
            "error_message": "Missing API key. Please set OPENWEATHER_API_KEY in your .env file.",
        }

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"].capitalize()
            temp_c = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            country = data["sys"]["country"]

            return {
                "status": "success",
                "report": (
                    f"The weather in {city.title()}, {country} is currently {weather} "
                    f"with a temperature of {temp_c}°C (feels like {feels_like}°C) "
                    f"and humidity of {humidity}%."
                ),
            }
        else:
            return {
                "status": "error",
                "error_message": f"Could not fetch weather data for {city}. "
                f"API message: {data.get('message', 'Unknown error')}",
            }

    except Exception as e:
        return {"status": "error", "error_message": str(e)}
