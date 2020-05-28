# Task 3
#
# The Weather app
# Write a console application which takes as an input a city name and returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use https://openweathermap.org

# open weather map lib
import pyowm
import configparser

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def weather(api_key):
	degree_sign = u'\N{DEGREE SIGN}'
	ow = pyowm.OWM(api_key)
	place_input = input(f"Enter the place:\t")
	place = ow.weather_at_place(place_input)  # obseration
	w = place.get_weather()  # get request with place
	temperature = w.get_temperature('celsius')
	status = w.get_status()
	icon = w.get_weather_icon_url()
	humidity = w.get_humidity()
	wind = w.get_wind()['speed']  # default meters per second

	return print("Weather in {} city | Temperature C: {}{} | Status: {} {} \nHumidity: {}\n Wind: {}"
		  .format(place_input, temperature['temp'], degree_sign, status, icon, humidity, wind))

if __name__ == "__main__":

	api_key = get_api_key()
	weather(api_key)