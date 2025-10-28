import requests
weather_api=''


api_keys='cba89ac28a03b715a00c1766491d984b'

#read (get)
city_name='goa'
resp_data=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_keys}')
print(resp_data) # <Response [200]> #<Response [401]>

python_data=resp_data.json()
print(type(python_data)) #<class 'dict'>
print(python_data)
# {'coord': {'lon': 74.0833, 'lat': 15.3333}, 'weather': [{'id': 802, 'main': 'Clouds', 
# 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 306.71, 
# 'feels_like': 308.58, 'temp_min': 306.71, 'temp_max': 306.71, 'pressure': 1009, 'humidity': 43,
# 'sea_level': 1009, 'grnd_level': 996}, 'visibility': 10000, 'wind': {'speed': 1.78, 'deg': 30, 
# 'gust': 3.46}, 'clouds': {'all': 31}, 'dt': 1760337000, 'sys': {'country': 'IN', 'sunrise': 1760316891, 
# 'sunset': 1760359481}, 'timezone': 19800, 'id': 1271157, 'name': 'Goa', 'cod': 200}