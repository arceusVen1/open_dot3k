#/usr/bin/python2.7

import dot3k.backlight as backlight
import sys
class Backlight():

	def __init__(self):
		self.maxtemp = 50.0
		self.mintemp = 10.0
		self.midtemp = 30.0
		self.step = 255.0 / ((self.maxtemp - self.mintemp)/2)

	def color(self, temp):
		try: 
			if temp <= self.midtemp:
				increment = int((temp - self.mintemp)  * self.step)
				green = 0 + increment
				blue = 255 - increment
				red = 0
				backlight.rgb(red, green, blue)
			elif temp > self.midtemp:
				increment = int((temp - self.midtemp)  * self.step)
				green = 255 - increment
				red = 0 + increment
				blue = 0
				backlight.rgb(red, green, blue)
		except:
			backlight.rgb(255, 255, 255)
			print "exception raised " + sys.exc_info() 

	def power_off(self):
		backlight.off()
