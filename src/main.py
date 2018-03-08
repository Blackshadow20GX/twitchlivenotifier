import requests
import json
import os
from model.data import Model
from controller.controller import Controller
from view.window import MainWindow

def main():

    model = Model("/config.json")
    url, headers = model.getConfig()
    view = MainWindow(url, headers)
    controller = Controller(model, view)
    
    view.displayWindow(controller)

if __name__ == "__main__":
    main()