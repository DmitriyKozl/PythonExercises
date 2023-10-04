import requests
from twilio.rest import Client
from dotenv import load_dotenv
from  dotenv import dotenv_values


config = dotenv_values('.env')
account_sid = "ACC_SID"
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)

OWM_endpoint = 'https://api.openweathermap.org/data/2.8/onecall'
api_key = 'API_KEY'
weather_params = {
    "lat": 51.053822,
    "lon": 3.722270,
    "appid": api_key,
    "exclude": "daily,current,minutely"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
curr_weather = data["hourly"][:12]
will_rain = False
for hour_data in curr_weather:
    if hour_data['weather'][0]['id'] < 700:
        will_rain = True

if will_rain == False:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="run around naked",
        from_='Phone',
        to='Phone'
    )
    print(message.status)

