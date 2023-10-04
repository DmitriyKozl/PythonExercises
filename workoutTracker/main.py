import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
app_id= os.environ.get('APP_ID')
auth_key = os.environ.get('API_KEY')
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    "x-app-id": app_id,
    "x-app-key": auth_key,
    "x-remote-user-id": "0"
}
input_exercise = input("What exercises did you do today?")
exercise_params ={
    "query": input_exercise,
    "gender": "male",
    "weight_kg":90 ,
    "height_cm": 182,
    "age": 30
}
response = requests.post(url=exercise_endpoint, json=exercise_params,headers=headers)
print(response.json())
today = datetime.now().strftime('%w/%m/%Y')
time = datetime.now().strftime('%H:%M')
print(today,time)
data_dict = {
    "Date":today ,
    "Time":time,
    "Exercise":"",
    "Duration":"",
    "Calories":"",
}