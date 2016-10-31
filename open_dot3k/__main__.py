#/usr/bin/python2.7

import dot3k.joystick as j
import time
import sys
import os
import signal
import screen, backlight, ledbar, temperature, joystick

MESSAGE = screen.Screen()
TEMP =  temperature.Temperature()
LED = ledbar.LedBar()
SCROLLER = joystick.Scroller()
LIGHT =  backlight.Backlight()


def main():
	if SCROLLER.scrollnum >= len(TEMP.temperatures):
		SCROLLER.reset()
	if SCROLLER.scrollnum < 0:
		SCROLLER.scrollnum = len(TEMP.temperatures) - 1
	MESSAGE.writeTemp(TEMP.temperatures[SCROLLER.scrollnum])
	LIGHT.color(float(TEMP.temperatures[SCROLLER.scrollnum]))
	LED.set_size(float(TEMP.temperatures[SCROLLER.scrollnum]))
	return

@j.on(j.UP)
def handle_up(pin):
	MESSAGE.clearScreen()
	TEMP.readTemp()
	main()
	
@j.on(j.RIGHT)
def handle_right(pin):
	MESSAGE.clearScreen()
	SCROLLER.rightSignal()
	main()


@j.on(j.LEFT)
def handle_left(pin):
	MESSAGE.clearScreen()
	SCROLLER.leftSignal()
	main()

@j.on(j.DOWN)
def handle_left(pin):
	MESSAGE.clearScreen()
	LIGHT.power_off()
	LED.ledZero()
	os.kill(os.getpid(), signal.SIGKILL)


signal.pause()

if __name__ == '__main__':
	sys.exit(main())
