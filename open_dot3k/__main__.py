#!/usr/bin/python3


import dothat.touch as t
import time
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
from open_ds18b20.probe import Materials

MESSAGE = screen.Screen()
TEMP = temperature.Temperature()
LED = ledbar.LedBar()
SCROLLER = joystick.Scroller()
LIGHT = backlight.Backlight()
VERROU1 = Lock()
VERROU2 = Lock()
IP = ip.IP()
MATERIALS = Materials()


def clean_and_write():
    probes = list(TEMP.temperatures.keys()) + list(TEMP.humidity.keys())
    if SCROLLER.scrollnum >= len(TEMP.temperatures) + len(TEMP.humidity) + len(TEMP.messages):
        SCROLLER.reset()
    elif SCROLLER.scrollnum < 0:
        SCROLLER.scrollnum = len(TEMP.temperatures) + len(TEMP.humidity) + len(TEMP.messages) - 1
    if SCROLLER.scrollnum >= len(TEMP.temperatures) +len(TEMP.humidity):
        LIGHT.color_alert()
        MESSAGE.write_message(TEMP.messages[SCROLLER.scrollnum - len(TEMP.temperatures) - len(TEMP.humidity)])
    else:
        probe = probes[SCROLLER.scrollnum]
        fprobe = MATERIALS.get_probe_by_slug(probe)
        if fprobe[0] is not None and fprobe[0]["alert"]["bool"]:
            max = fprobe[0]["alert"]["max"]
            min = fprobe[0]["alert"]["min"]
        else:
            max = None
            min = None
        if SCROLLER.scrollnum < len(TEMP.temperatures):
            MESSAGE.write_temp(probe, TEMP.temperatures[probe], IP.address, TEMP.time_of_read)
            LIGHT.color(float(TEMP.temperatures[probe]), max, min)
            LED.set_size(float(TEMP.temperatures[probe]), max)
        elif len(TEMP.humidity) + len(TEMP.temperatures) > SCROLLER.scrollnum >= len(TEMP.temperatures):
            MESSAGE.write_humidity(probe, TEMP.humidity[probe], IP.address, TEMP.time_of_read)
            LIGHT.color(float(TEMP.humidity[probe]), max, min)
            LED.set_size(float(TEMP.humidity[probe]), max)
    return


class Display(Thread):
    """docstring for Display"""

    def __init__(self):
        MATERIALS.allow_config()
        MATERIALS.get_data()
        Thread.__init__(self)

    def run(self):
        @t.on(t.UP)
        def handle_up(ch, evt):
            VERROU2.acquire()
            MESSAGE.clear_screen()
            TEMP.read_temp()
            clean_and_write()
            VERROU2.release()

        @t.on(t.RIGHT)
        def handle_right(ch, evt):
            VERROU2.acquire()
            MESSAGE.clear_screen()
            SCROLLER.right_signal()
            clean_and_write()
            VERROU2.release()

        @t.on(t.LEFT)
        def handle_left(ch, evt):
            VERROU2.acquire()
            MESSAGE.clear_screen()
            SCROLLER.left_signal()
            clean_and_write()
            VERROU2.release()

        @t.on(t.DOWN)
        def handle_down(ch, evt):
            VERROU2.acquire()
            MESSAGE.clear_screen()
            LIGHT.power_off()
            LED.led_zero()
            VERROU2.release()

        @t.on(t.BUTTON)
        def handle_button(ch, evt):
            pass

        @t.on(t.CANCEL)
        def handle_cancel(ch, evt):
            pass

        signal.pause()


class Measure(Thread):
    """docstring for Measure"""

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            VERROU1.acquire()
            MESSAGE.clear_screen()
            IP.get_address()
            TEMP.read_temp()
            if len(TEMP.messages) > 0:
                clean_and_write()
            else:
                LIGHT.power_off()
            VERROU1.release()
            time.sleep(300)
        return


def out(signal, frame):
    MESSAGE.clear_screen()
    MESSAGE.write_message("out !")
    time.sleep(3)
    LED.led_zero()
    LIGHT.power_off()
    MESSAGE.clear_screen()
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
