from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Singapore"):
    request_rul = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"

    weather_data = requests.get(request_rul).json()

    return weather_data

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Singapore"

    wheather_data = get_current_weather(city)

    print("\n")
    pprint(wheather_data)