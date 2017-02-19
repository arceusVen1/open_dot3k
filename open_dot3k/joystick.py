#!/usr/bin/python3


class Scroller():

    def __init__(self):
        self.scrollnum = 0
        return

    def right_signal(self):
        self.scrollnum += 1

    def left_signal(self):
        self.scrollnum -= 1

    def reset(self):
        self.scrollnum = 0
