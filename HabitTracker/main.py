import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os
username= os.environ.get('USERNAME')
token = os.environ.get('TOKEN')
graph_id =os.environ.get('GRAPH_ID')

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {"token": token,
               "username": username,
               "agreeTermsOfService": "yes",
               "notMinor": "yes", }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'
graph_config = {
    "id": graph_id,
    "name": "CyclingGraph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)
today =datetime.now()
pixela_endpoint_creation = f'{pixela_endpoint}/{username}/graphs/{graph_id}'
pixel_data={
    "date":today.strftime('%Y%m%d'),
    "quantity": "9.33",
}

response = requests.post(url=pixela_endpoint_creation,json=pixel_data,headers=headers)
print(response.text)