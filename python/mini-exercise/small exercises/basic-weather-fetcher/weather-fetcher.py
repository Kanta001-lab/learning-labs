import requests

def get_weather(city):
    """Get weather for any city using wrttr.in API"""
    url = f"https://wttr.in/{city}?format=%C|%t|%w|%h"

    response = requests.get(url)


    if response.status_code == 200:
        condition, temp, wind, humidity = response.text.split('|')
        print(f"\n WEATHER FOR {city.upper()}")
        print("=" * 30)
        print(f"Condition: {condition}")
        print(f"Temperature: {temp}")
        print(f"Wind: {wind}")
        print(f"Humidity: {humidity}")
        return {"condition": condition, "temp": temp, "wind": wind, "humidity": humidity}
    else:
        print(f"❌ Could not fetch weather for {city}")
        return None
    
if __name__ == "__main__":
    get_weather("Tokyo")
    get_weather("Lagos")
    get_weather("Germany")
    get_weather("Greenland")