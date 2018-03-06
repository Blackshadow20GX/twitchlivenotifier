import requests
import json
import os
from controller.notifier import notifier
from view.window import instantiate

def main():
    config_path = "/config.json"
    rwd = os.path.dirname(os.path.realpath(__file__))
    rwd = os.path.split(rwd)[0]

    with open(rwd + config_path, "r") as json_data:
        config = json.load(json_data)

    url = config['url']
    headers = config['headers']

    instantiate(url, headers)

if __name__ == "__main__":
    main()