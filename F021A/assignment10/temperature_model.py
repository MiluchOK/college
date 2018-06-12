from enum import Enum


class Temperature:
	def __init__(self, temp, unit):
		self.temp = temp
		self.unit = unit

	def to_celsius(self):
		if self.unit == 'celsius':
			return self.temp
		else:
			# Formula
			return 100

	def to_fahrenheit(self):
		if self.unit == 'fahrenheit':
			return self.temp
		else:
			# Formula
			return 100


class TemperatureType(Enum):
	fahrenheit = 'fahrenheit'
	celsius = 'celsius'
