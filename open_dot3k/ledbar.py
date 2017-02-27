#!/usr/bin/python3

import dothat.backlight as backlight


class LedBar():

    def __init__(self):
        pass

    def set_size(self, value, max):
        if max is None:
            max = 50
        for i in range(int(value)):
            backlight.set_graph(i / max)

    def led_zero(self):
        backlight.set_graph(0)
