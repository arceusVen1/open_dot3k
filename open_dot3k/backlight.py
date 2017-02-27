#!/usr/bin/python3

import dothat.backlight as backlight


class Backlight():

    def __init__(self):
        pass

    def color(self, value, max, min):
        if max and min:
            mid = min + (max-min)/2
            step = 255.0 / ((max - min)/ 2)
        try:
            if value <= mid:
                increment = int((value - min) * step)
                green = 0 + increment
                blue = 255 - increment
                red = 0
                backlight.rgb(red, green, blue)
            elif value > mid:
                increment = int((value - mid) * step)
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
