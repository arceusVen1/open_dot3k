#!/usr/bin/python3

import dothat.backlight as backlight


class LedBar():

    def __init__(self):
        self.maxtemp = 50.0  # warning: maxtemp must be a float !
        return

    def set_size(self, temp):
        for i in range(int(temp)):
            backlight.set_graph(i / self.maxtemp)

    def led_zero(self):
        backlight.set_graph(0)
