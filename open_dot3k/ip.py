#!/usr/bin/python3


import netifaces as ni


class IP():
    """represent the ip adress"""

    def __init__(self):
        self.address = ""

    def get_address(self):
        try:
            self.address = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        except:
            pass
        try:
            self.address = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
        except:
            self.address = "Not connected"
