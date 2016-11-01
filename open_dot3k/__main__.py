#/usr/bin/python3

import dot3k.joystick as j
import time
import sys
import os
import signal
from threading import Thread, RLock
import screen, backlight, ledbar, temperature, joystick

MESSAGE = screen.Screen()
TEMP =  temperature.Temperature()
LED = ledbar.LedBar()
SCROLLER = joystick.Scroller()
LIGHT =  backlight.Backlight()
VERROU = RLock()

def cleanAndWrite():
	if SCROLLER.scrollnum >= len(TEMP.temperatures):
		SCROLLER.reset()
	if SCROLLER.scrollnum < 0:
		SCROLLER.scrollnum = len(TEMP.temperatures) - 1
	MESSAGE.writeTemp(TEMP.temperatures[SCROLLER.scrollnum])
	LIGHT.color(float(TEMP.temperatures[SCROLLER.scrollnum]))
	LED.set_size(float(TEMP.temperatures[SCROLLER.scrollnum]))
	return


class Display(Thread):
	"""docstring for Display"""
	def __init__(self):
		Thread.__init__()
	
	def run(self):
		@j.on(j.UP)
		def handle_up(pin):
			MESSAGE.clearScreen()
			TEMP.readTemp()
			cleanAndWrite()
	
		@j.on(j.RIGHT)
		def handle_right(pin):
			MESSAGE.clearScreen()
			SCROLLER.rightSignal()
			cleanAndWrite()


		@j.on(j.LEFT)
		def handle_left(pin):
			MESSAGE.clearScreen()
			SCROLLER.leftSignal()
			cleanAndWrite()

		@j.on(j.DOWN)
		def handle_left(pin):
			MESSAGE.clearScreen()
			LIGHT.power_off()
			LED.ledZero()
			os.kill(os.getpid(), signal.SIGKILL)


		signal.pause()

class Measure(Thread):
	"""docstring for Measure"""
	def __init__(self):
		Thread.__init__()
		
	def run():
		with VERROU:
			MESSAGE.clearScreen()
			TEMP.readTemp()
			cleanAndWrite()
		time.sleep(300)



def main():
	Measure.start()
	Display.start()

if __name__ == '__main__':
	sys.exit(main())
