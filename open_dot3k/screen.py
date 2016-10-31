#/usr/bin/python2.7


import dot3k.lcd as lcd

class Screen():

	def __init__(self):
		lcd.clear()
		self.content = ""
	
	def writeTemp(self, temp):
		self.content = "il fait " + str(temp) + "*C"
		lcd.write(self.content)

	def clearScreen(self):
		lcd.clear()


