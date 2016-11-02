#!/usr/bin/python3


class Scroller():

    def __init__(self):
        self.scrollnum = 0
        return

    def rightSignal(self):
        self.scrollnum += 1

    def leftSignal(self):
        self.scrollnum -= 1

    def reset(self):
        self.scrollnum = 0
