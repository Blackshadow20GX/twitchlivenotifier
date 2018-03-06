import requests
import json
import os
import time

def main():
    config_path = "/config.json"

    rwd = os.path.dirname(os.path.realpath(__file__))
    rwd = os.path.split(rwd)[0]

    with open(rwd + config_path, "r") as json_data:
        config = json.load(json_data)

    url = config['url']
    headers = {"Client-ID": config['client_id']}

    streamLoop(url, headers)

def checkStreamStatus(url, headers):

    r = requests.get(url, headers=headers)
    live = r.json()["stream"]

    if(live is None):
        print("Stream is offline :(")
    else:
        print("Stream is online!")

        
    return

def streamLoop(url, headers):
    count = 1
    seconds = 5
    while(True):
        print("Round " + str(count) + ", FIGHT!")
        print("Checking status of " + url + "...")
        checkStreamStatus(url, headers)
        print("Sleeping for " + str(seconds) + " seconds...")
        count += 1
        time.sleep(seconds)

if __name__ == "__main__":
    main()
