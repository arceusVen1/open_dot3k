#!/usr/bin/python3
from open_ds18b20.__main__ import main as acqtemp
from datetime import datetime


class Temperature():

    def __init__(self):
        self.temperatures = {}
        self.humidity = {}
        self.messages = []
        self.time_of_read = ""
        return

    def read_temp(self):
        result = acqtemp()
        self.temperatures = result[0]
        self.humidity = result[1]
        self.messages = result[2]
        self.time_of_read = datetime.now().strftime("%H:%M")
