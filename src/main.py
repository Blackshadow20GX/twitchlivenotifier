import requests
import json
import os
from model.data import Model
from controller.controller import notifier
from view.window import MainWindow, instantiateView

def main():

    model = Model("/config.json")
    url, headers = model.getConfig()
    instantiateView(url, headers)

if __name__ == "__main__":
    main()