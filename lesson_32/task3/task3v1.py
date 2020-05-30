# Task 3
#
# The Weather app
# Write a console application which takes as an input a city name and returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use https://openweathermap.org


import requests

degree_sign = u'\N{DEGREE SIGN}'
city = input('Enter your city:\t')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={API}&units=metric'.format(city)
res = requests.get(url)
data = res.json()

if __name__ == "__main__":
    if res.ok:
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']

        print("Temperature: {}{}".format(temp, degree_sign))
        print("Wind: {} m/s".format(wind_speed))
        print("Description: {}".format(description))
        print("Humidity: {}".format(humidity))
        print("Latitude: {}\nLangitude: {}".format(latitude, longitude))
    else:
        print("Url: {} not response {} or mistake in input city ".format(url, res))
        raise ConnectionError


