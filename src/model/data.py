import os
import json

class Model():

    def __init__(self, config_path):
        self.online = False
        self.config_path = config_path
        self.url = None
        self.headers = None
        self.readConfig()

    def readConfig(self):
        rwd = os.path.dirname(os.path.realpath(__file__))
        rwd = os.path.split(rwd)[0]

        with open(rwd + self.config_path, "r") as json_data:
            config = json.load(json_data)

        self.url = config['url']
        self.headers = config['headers']

    def getUrl(self):
        return self.url

    def getHeaders(self):
        return self.headers

    def isOnline(self):
        return self.online

    def setStatus(self, status):
        self.online = status