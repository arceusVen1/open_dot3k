#!/usr/bin/python3

import dothat.backlight as backlight


class Backlight():

    def __init__(self):
        self.maxtemp = 50.0
        self.mintemp = 10.0
        self.midtemp = 30.0
        self.step = 255.0 / ((self.maxtemp - self.mintemp) / 2)

    def color(self, temp):
        try:
            if temp <= self.midtemp:
                increment = int((temp - self.mintemp) * self.step)
                green = 0 + increment
                blue = 255 - increment
                red = 0
                backlight.rgb(red, green, blue)
            elif temp > self.midtemp:
                increment = int((temp - self.midtemp) * self.step)
                green = 255 - increment
                red = 0 + increment
                blue = 0
                backlight.rgb(red, green, blue)
        except:
            self.color_alert()
            # print("exception raised " + sys.exc_info())

    def color_alert(self):
        backlight.rgb(255, 0, 0)

    def power_off(self):
        backlight.off()
