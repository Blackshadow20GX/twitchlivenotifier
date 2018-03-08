import requests
import json
import os
import time

online = False

def notifier(url, headers):
    checkStreamStatus(url, headers)
    return None

def checkStreamStatus(url, headers):
    print("Checking status of " + url + "...")
    r = requests.get(url, headers=headers)
    live = r.json()["stream"]

    if(live is None):
        print("Stream is offline :(")
    else:
        print("Stream is online!")
    
    setStatus(live)

def isOnline():
    return online

def setStatus(status):
    online = status
