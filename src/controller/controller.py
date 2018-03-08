import requests
import json
import os
import time

class Controller():

    def __init__(self, model, view, url, headers):
        self.model = model
        self.view = view
        self.url = url
        self.headers = headers

    def checkStreamStatus(self):
        print("Checking status of " + self.url + "...")
        r = requests.get(self.url, headers=self.headers)
        status = r.json()["stream"]

        if(status is None):
            print("Stream is offline :(")
            status = False
        else:
            print("Stream is online!")
            status = True
        
        self.setStatus(status)

    def isOnline(self):
        return self.model.isOnline()

    def setStatus(self, status):
        self.model.setStatus(status)
