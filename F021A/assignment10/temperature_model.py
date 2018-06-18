"""
The model for temperature conversion program
"""

from enum import Enum


class Temperature:
	def __init__(self, temp, unit):
		"""
		The Module constructor
		:param temp: int value for the temperature
		:param unit: type value for the temperature
		"""
		self.temp = temp
		self.unit = unit

	def get_value(self):
		"""
			Get the temperature value
		"""
		return self.temp

	def convert_to(self, unit):
		"""
			Convert to another unit
		:param unit: type to convert TO
		:return: returns self in changed state
		"""
		converter_map = {
			TemperatureType.celsius: self._to_celsius,
			TemperatureType.fahrenheit: self._to_fahrenheit
		}

		return converter_map[unit]()

	def _to_celsius(self):
		"""
			Convert the temperature to Celsius
		"""
		if self.unit != TemperatureType.celsius:
			self.unit = TemperatureType.celsius
			print("Current temp: {}".format(self.temp))
			self.temp = (5 / 9) * (self.temp - 32)
		return self

	def _to_fahrenheit(self):
		"""
			Convert the temperature to Fahrenheit
		"""
		if self.unit != TemperatureType.fahrenheit:
			self.unit = TemperatureType.fahrenheit
			self.temp = ((9 / 5) * self.temp) + 32
		return self


"""
The types of temperatures supported by the program
"""
class TemperatureType(Enum):
	fahrenheit = 'fahrenheit'
	celsius = 'celsius'
