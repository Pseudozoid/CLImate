import argparse
import pyfiglet
import sys
import requests
from simple_chalk import chalk
from tabulate import tabulate
from config import get_api_key

API_KEY = get_api_key()
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather' 

WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

if len(sys.argv) < 2:
    print('Usage: climate <location> [--color <color>]')
    exit(1)

else:
    parser = argparse.ArgumentParser(description="Check weather for country/city")
    parser.add_argument("country", help="Country/city to check weather for")
    parser.add_argument("-c", "--color", default="green", help="Color for the output text")
    parser.add_argument("-f", "--font", default="standard", help="Font of the city name")
    args = parser.parse_args()
    url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"
    
    VALID_COLORS = [
        "red", "green", "yellow", "blue", "magenta", "cyan", "white", "black",
    ]

    VALID_FONTS = pyfiglet.FigletFont.getFonts()

    if args.color not in VALID_COLORS:
        print(chalk.red(f"Invalid color: {args.color}. Valid colors are: {', '.join(VALID_COLORS)}"))
        exit(1)

    if args.font not in VALID_FONTS:
        print(chalk.red(f"Invalid font: {args.font}. See http://www.figlet.org/fontdb.cgi for list of valid fonts"))
        exit(1)

    # Make and parse API request
    response = requests.get(url)
    if response.status_code != 200:
        print(chalk.red("Unable to retrive weather data!"))
        exit(1)

    data = response.json()
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    city = data["name"]
    country = data["sys"]["country"]
    humidity = data["main"]["humidity"]

    # output
    weather_icon = WEATHER_ICONS.get(icon, "")
    output = f"{pyfiglet.figlet_format(city, font=args.font)}"
    output += f"{weather_icon} {description}"
    weather_data = [
        ["Country", country],
        ["Temperature", f"{temperature}°C"],
        ["Feels like", f"{feels_like}°C"],
        ["Humidity", humidity],
    ]

    formatted_output = getattr(chalk, args.color)(output)
    print(formatted_output)
    print(getattr(chalk, args.color)(tabulate(weather_data, tablefmt="grid")))

