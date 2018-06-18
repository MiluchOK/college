import tkinter
import temperature_model


class TemperatureController:
	"""
	The CONTROLLER for an app that follows the Model/View/Controller architecture.
	"""

	def __init__(self):
		"""
		The constructor for the controller
		"""
		self.temp_types = [temperature_model.TemperatureType.fahrenheit.name,
						   temperature_model.TemperatureType.celsius.name]

	def convertButtonPressed(self, value_to_convert, convert_from_type, convert_to_type, resulting_element):
		"""
		The temperature conversion function
		:param value_to_convert: Integer value to convert
		:param convert_from_type: Type of Temperature to convert FROM
		:param convert_to_type: Type of Temperature to conver TO
		:param resulting_element: The element that is going to be set with the result
		:return: null
		"""

		from_type = temperature_model.TemperatureType[convert_from_type]
		to_type = temperature_model.TemperatureType[convert_to_type]

		value = value_to_convert

		if from_type != to_type:
			temperature = temperature_model.Temperature(int(value_to_convert), from_type)
			value = temperature.convert_to(to_type).get_value()

		resulting_element.configure(state='normal')
		resulting_element.delete(0, 'end')
		resulting_element.insert(0, value)
		resulting_element.configure(state='readonly')

	def get_possible_temp_states(self):
		"""
		the function returns all the supported temperature types
		:return:
		"""
		return self.temp_types
