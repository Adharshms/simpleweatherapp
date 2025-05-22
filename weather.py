import requests

API_KEY = "9fcf8bf884044d0292c090bc6d03243a"
  # replace this with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n📍 Weather in {city.title()}:")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌬 Wind Speed: {data['wind']['speed']} m/s")
        print(f"⛅ Condition: {data['weather'][0]['description'].title()}")
    else:
        print("⚠️ City not found or error fetching data.")

def main():
    print("🌦️ Welcome to the Weather Checker CLI")
    while True:
        city = input("\nEnter a city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        get_weather(city)

if __name__ == "__main__":
    main()
