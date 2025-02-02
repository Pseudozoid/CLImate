# CLImate 🌦️ 
<img src="https://i.imgur.com/Njop9FV.jpeg" alt="climate" align="centre">

Pretty printed weather data for your terminal with customizable colours and fonts that I built while learning Python. Based on [this](https://github.com/BekBrace/weather-app-cli-python) project by [BekBrace](https://github.com/BekBrace) with added features and improvements.

## Requirements ⚙️
- **Python 3.6+**
- **API Key** from OpenWeather (See [Installation](#Installation))

## Installation 📦
### Obtaining API Key
1. Create an [OpenWeather](https://openweathermap.org/) account (it's free)
2. Click on your account name in the top banner then go to 'My API keys'
3. Copy your API key

### Package Installation
1. Clone this repo to your local machine
2. cd into the cloned repo
3. Run ```pip install .```
4. After the installation, run ```climate```
5. You will be prompted to enter your API key. Paste your API key that you obtained earlier.

## Usage 📜
Once installed, you can use the climate command from anywhere in your terminal.

```climate <location> [--color <color>] [--font <font>]```
- **location**: Name of the city or country you want to check the weather for.

- **--color**: Optional. Choose the color of the output text
  (options: ```red```, ```green```, ```yellow```, ```blue```, ```magenta```, ```cyan```, ```white```, ```black```).

- **--font**: Optional. Choose the font style for the city name header. See the [figlet font list](http://www.figlet.org/fontdb.cgi) page for a list of valid font names.
 
## Contributing 🤝
Feel free to fork the repository and submit a pull request with your improvements or bug fixes, or raise an issue for suggestions and feature requests.

## License 📄
CLImate is open-source software licensed under the [MIT License](https://github.com/Pseudozoid/CLImate/blob/main/LICENSE).

## Contact 📬
For any questions or suggestions you can reach me at sarathmadhavr@gmail.com.
