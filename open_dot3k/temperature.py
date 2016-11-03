#!/usr/bin/python3
from open_ds18b20.__main__ import main as acqtemp


class Temperature():

    def __init__(self):
        self.temperatures = []
        self.messages = []
        return

    def readTemp(self):
        result = acqtemp()
        self.temperatures = result["temperatures"]
        self.messages = result["messages"]
