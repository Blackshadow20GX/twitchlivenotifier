import requests
import json
import os
import time

class Controller():

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def notifier(self, url, headers):
        self.checkStreamStatus(url, headers)
        return None

    def checkStreamStatus(self, url, headers):
        print("Checking status of " + url + "...")
        r = requests.get(url, headers=headers)
        status = r.json()["stream"]

        if(status is None):
            print("Stream is offline :(")
        else:
            print("Stream is online!")
        
        self.setStatus(status)

    def isOnline(self):
        return self.model.isOnline()

    def setStatus(self, status):
        self.model.setOnline(status)
