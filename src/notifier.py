import requests
import json
import os

config_path = "/config.json"

rwd = os.path.dirname(os.path.realpath(__file__))
rwd = os.path.split(rwd)[0]

with open(rwd + config_path, "r") as json_data:
    config = json.load(json_data)

url = config['url']
headers = {"Client-ID": config['client_id']}

r = requests.get(url, headers=headers)
print(r.json())