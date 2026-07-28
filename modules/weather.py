import requests

API_KEY = "YOUR_OPENWEATHER_KEY"
CITY = "London"

def get_weather():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={CITY}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    # If API returned an error, show it safely
    if "main" not in data or "weather" not in data:
        return {
            "location": CITY,
            "temperature": "N/A",
            "condition": data.get("message", "Unavailable").title()
        }

    return {
        "location": CITY,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"].title()
    }
