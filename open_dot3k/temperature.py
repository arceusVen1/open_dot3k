#/usr/bin/python2.7
from open_ds18b20.__main__ import main as acqtemp

class Temperature():

	def __init__(self):
		self.temperatures = []
		return
	
	def readTemp(self):
		self.temperatures = acqtemp()
		return

	
		
		
