#/usr/bin/python2.7

import dot3k.backlight as backlight

class LedBar():

	def __init__(self):
		self.maxtemp = 50.0 #warning: maxtemp must be a float !
		return

	def set_size(self, temp):
		for i in range(int(temp)):
			backlight.set_graph(i/self.maxtemp)


	def ledZero(self):
		backlight.set_graph(0)
