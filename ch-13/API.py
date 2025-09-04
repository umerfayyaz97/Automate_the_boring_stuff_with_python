import requests
import json

city_name = 'San Francisco'
state_code = 'CA'
country_code = 'US'

API_key = 'a724681d17e118722e160811fd8ea2a1'

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')

# print(type(response.text))
response_data = json.loads(response.text)

print(response_data[0]['lat'])