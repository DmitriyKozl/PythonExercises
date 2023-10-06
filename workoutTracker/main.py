import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import pandas
import csv

load_dotenv()
app_id = os.environ.get('APP_ID')
auth_key = os.environ.get('API_KEY')
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    "x-app-id": app_id,
    "x-app-key": auth_key,
    "x-remote-user-id": "0"
}
input_exercise = input("What exercises did you do today?")
exercise_params = {
    "query": input_exercise,
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 182,
    "age": 30
}
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
data = response.json()
# exercises = data['exercises'][0]
# print(exercises['nf_calories'])
today = datetime.now().strftime('%w/%m/%Y')
time = datetime.now().strftime('%H:%M')
for exercise in data["exercises"]:
    data_dict = {
            "Date": today,
            "Time": time,
            "Exercise": exercise['name'],
            "Duration": exercise['duration_min'],
            "Calories": exercise['nf_calories']
        }

print(data_dict)

workout_data = pandas.DataFrame([data_dict])
workout_data.to_csv("workout.csv")
for (index, row) in workout_data.iterrows():
    print(row.count)
