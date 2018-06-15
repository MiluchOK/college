from enum import Enum


class Temperature:
	def __init__(self, temp, unit):
		self.temp = temp
		self.unit = unit

	"""
	Get the temperature value
	"""
	def get_value(self):
		return self.temp

	"""
	Convert to another unit
	"""
	def convert_to(self, unit):
		converter_map = {
			TemperatureType.celsius: self._to_celsius,
			TemperatureType.fahrenheit: self._to_fahrenheit
		}

		return converter_map[unit]()


	"""
	Convert the temperature to Celsius
	"""
	def _to_celsius(self):
		if self.unit != TemperatureType.celsius:
			self.unit = TemperatureType.celsius
			print("Current temp: {}".format(self.temp))
			self.temp = (5/9)*(self.temp-32)
		return self

	"""
	Convert the temperature to Fahrenheit
	"""
	def _to_fahrenheit(self):
		if self.unit != TemperatureType.fahrenheit:
			self.unit = TemperatureType.fahrenheit
			self.temp = ((9/5)*self.temp)+32
		return self


class TemperatureType(Enum):
	fahrenheit = 'fahrenheit'
	celsius = 'celsius'
