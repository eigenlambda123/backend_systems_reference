import httpx
from functools import lru_cache
from typing import Dict

API_KEY = "your_api_key" # dummy API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@lru_cache(maxsize=100) # Cache up to 100 unique city weather requests

def get_weather(city: str) -> Dict:
    """"Fetches weather data for a given city, using an LRU cache to store results"""

    print(f"Fetching weather for {city}...")
    response = httpx.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch weather: {response.text}")

    return response.json()


# Example usage
city = "Manila"
print(get_weather(city))  # Will fetch from the API
print(get_weather(city))  # Will use the cache

print(get_weather.cache_info()) # Display cache statistics
get_weather.cache_clear() # Clear the cache
