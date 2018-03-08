import requests
import json
import os
from model.data import Model
from controller.controller import Controller
from view.window import MainWindow

def main():

    model = Model("/config.json")
    url, headers = model.getUrl(), model.getHeaders()
    
    view = MainWindow()
    controller = Controller(model, view, url, headers)

    view.displayWindow(controller)

if __name__ == "__main__":
    main()