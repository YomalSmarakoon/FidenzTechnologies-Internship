from flask import Flask, jsonify
import json
import requests

app = Flask(__name__)
mainList=[]
weatherList = {"country": "",
               "sunrise": "",
               "sunset": "",
               "weatherMain": "",
               "weatherDescription": "",
               "mainTemp": "",
               "mainPressure": "",
               "mainHumidity": "",
               "mainTemp_min": "",
               "mainTemp_max": "",
               "visibility": "",
               "wind": "",
               "windDegree": "",
               "cloudsAll": "",
               "dt": "",
               "apiId": "",
               "cityName": ""
               }


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getcityinfo')
def get_city_info():
    return gellAllCityWeather()


def gellAllCityWeather():
    mainList.clear()
    cityIdList = []
    # with json load  (file)
    citiesInfo = open('cities.json', )
    data = json.load(citiesInfo)
    for row in data['List']:
        cityIdList.append(row['CityCode'])
    for element in cityIdList:
        cityId = element
        URL = "http://api.openweathermap.org/data/2.5/group"
        PARAMS = {'id': cityId, 'units': 'metric', 'appid': 'd24dc918b9743a49c0bd521aa67bac0c'}

        r = requests.get(url=URL, params=PARAMS)
        apiData = r.json()
        weatherList['country'] = apiData['list'][0]['sys']['country']
        weatherList['sunrise'] = apiData['list'][0]['sys']['sunrise']
        weatherList['sunset'] = apiData['list'][0]['sys']['sunset']

        weatherList['weatherMain'] = apiData['list'][0]['weather'][0]['main']
        weatherList['weatherDescription'] = apiData['list'][0]['weather'][0]['description']

        weatherList['mainTemp'] = apiData['list'][0]['main']['temp']
        weatherList['mainPressure'] = apiData['list'][0]['main']['pressure']
        weatherList['mainHumidity'] = apiData['list'][0]['main']['humidity']
        weatherList['mainTemp_min'] = apiData['list'][0]['main']['temp_min']
        weatherList['mainTemp_max'] = apiData['list'][0]['main']['temp_max']

        weatherList['visibility'] = apiData['list'][0]['visibility']
        weatherList['wind'] = apiData['list'][0]['wind']['speed']
        weatherList['windDegree'] = apiData['list'][0]['wind']['deg']
        weatherList['cloudsAll'] = apiData['list'][0]['clouds']['all']

        weatherList['dt'] = apiData['list'][0]['dt']
        weatherList['apiId'] = apiData['list'][0]['id']
        weatherList['cityName'] = apiData['list'][0]['name']
        mainList.append(weatherList)
        print(mainList)
    return jsonify(mainList)


if __name__ == '__main__':
    app.run(debug=True)
