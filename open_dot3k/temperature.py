#/usr/bin/python3
from open_ds18b20.__main__ import main as acqtemp

class Temperature():

	def __init__(self):
		self.temperatures = []
		self.message = ""
		return
	
	def readTemp(self):
		result = acqtemp()
		if isinstance(result, list):
			self.temperatures=result
			return self.temperatures
		else:
			self.message = result
		return self.message

	
		
		
