#!/usr/bin/python3
# Imports
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

MY_API_KEY = os.getenv("MY_API_KEY")

SMARTREAD_GET_TASK_ENDPOINT = "https://app-staging.smartread.jp/endpoints/hwr/v3beta1/task?offset=0&limit=10"
# MY_API_KEY = "3533038b-c9ff-4ba2-be91-da7e857b67ac"
def get_task():
    # Send GET request to SmartRead service
    response = requests.get(SMARTREAD_GET_TASK_ENDPOINT,
                            headers={'Authorization': 'apikey {}'.format(MY_API_KEY)})

    # Print the result
    # print(response.json())
    json_data = response.json()
    with open('getTask.json', 'w') as json_file:
        json.dump(json_data, json_file)
    
get_task()