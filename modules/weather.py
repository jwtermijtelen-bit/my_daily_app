import requests

API_KEY = "d1ac1ca47332a3810f1f70c25b5d0955"
CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    response = requests.get(URL)
    data = response.json()

    return {
        "location": CITY,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"].title()
    }
