import os
import json

class Model():

    def __init__(self, CONFIG_PATH):
        self.online = False
        self.CONFIG_PATH = CONFIG_PATH
        self.url = None
        self.headers = None
        self.readConfig()

    def readConfig(self):
        rwd = os.path.dirname(os.path.realpath(__file__))
        rwd = os.path.split(rwd)[0]

        with open(rwd + self.CONFIG_PATH, "r") as json_data:
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