#!/usr/bin/python3


import dothat.touch as t
import time
from datetime import datetime
import sys
import os
import signal
from threading import Thread, Lock
import screen
import backlight
import ledbar
import temperature
import joystick
import ip

MESSAGE = screen.Screen()
TEMP = temperature.Temperature()
LED = ledbar.LedBar()
SCROLLER = joystick.Scroller()
LIGHT = backlight.Backlight()
VERROU1 = Lock()
VERROU2 = Lock()
IP = ip.IP()


def cleanAndWrite():
    probes = list(TEMP.temperatures.keys())
    time = datetime.now().strftime("%H:%M")
    if SCROLLER.scrollnum >= len(TEMP.temperatures) + len(TEMP.messages):
        SCROLLER.reset()
    elif SCROLLER.scrollnum < 0:
        SCROLLER.scrollnum = len(TEMP.temperatures) + len(TEMP.messages) - 1
    if SCROLLER.scrollnum < len(TEMP.temperatures):
        probe = probes[SCROLLER.scrollnum]
        MESSAGE.writeTemp(probe, TEMP.temperatures[probe], IP.address, time)
        LIGHT.color(float(TEMP.temperatures[probe]))
        LED.set_size(float(TEMP.temperatures[probe]))
    else:
        LIGHT.colorAlert()
        MESSAGE.writeMessage(
            TEMP.messages[SCROLLER.scrollnum - len(TEMP.temperatures)])
    return


class Display(Thread):
    """docstring for Display"""

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        @t.on(t.UP)
        def handle_up(ch, evt):
            VERROU2.acquire()
            MESSAGE.clearScreen()
            TEMP.readTemp()
            cleanAndWrite()
            VERROU2.release()

        @t.on(t.RIGHT)
        def handle_right(ch, evt):
            VERROU2.acquire()
            MESSAGE.clearScreen()
            SCROLLER.rightSignal()
            cleanAndWrite()
            VERROU2.release()

        @t.on(t.LEFT)
        def handle_left(ch, evt):
            VERROU2.acquire()
            MESSAGE.clearScreen()
            SCROLLER.leftSignal()
            cleanAndWrite()
            VERROU2.release()

        @t.on(t.DOWN)
        def handle_down(ch, evt):
            VERROU2.acquire()
            MESSAGE.clearScreen()
            LIGHT.power_off()
            LED.ledZero()
            VERROU2.release()
        signal.pause()


class Measure(Thread):
    """docstring for Measure"""

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            VERROU1.acquire()
            MESSAGE.clearScreen()
            IP.get_address()
            TEMP.readTemp()
            if len(TEMP.messages) > 0:
                cleanAndWrite()
            else:
                LIGHT.power_off()
            VERROU1.release()
            time.sleep(300)
        return


def out(signal, frame):
    MESSAGE.clearScreen()
    MESSAGE.writeMessage("out !")
    time.sleep(3)
    LED.ledZero()
    LIGHT.power_off()
    MESSAGE.clearScreen()
    os.kill(os.getpid(), signal.SIGKILL)
    sys.exit(0)


def main():
    Measure().start()
    time.sleep(1)
    Display().start()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, out)
    signal.signal(signal.SIGTERM, out)
    main()
