import tkinter
import temperature_model
import temperature_view


class TemperatureController:
	"""
	The CONTROLLER for an app that follows the Model/View/Controller architecture. When the user presses a Button on the View, this Controller calls the appropriate methods in the Model. The Controller handles all communication between the Model and the View.
	"""

	def __init__(self):
		"""
		This starts the Tk framework up, instantiates the Model (a Counter object), instantiates the View (a MyFrame object), and starts the event loop that waits for the user to press a Button on the View.
		"""
		self.temp_types = [temperature_model.TemperatureType.fahrenheit.name,
						   temperature_model.TemperatureType.celsius.name]

	def convertButtonPressed(self, value_to_convert, convert_from_type, convert_to_type, resulting_element):
		"""
		Python calls this method when the user presses the incrementButton in the View.
		"""

		from_type = temperature_model.TemperatureType[convert_from_type]
		to_type = temperature_model.TemperatureType[convert_to_type]

		print("FROM {}".format(from_type))
		print("TO {}".format(to_type))

		value = value_to_convert

		if from_type != to_type:
			temperature = temperature_model.Temperature(int(value_to_convert), from_type)
			value = temperature.convert_to(to_type).get_value()

		resulting_element.configure(state='normal')
		resulting_element.delete(0, 'end')
		resulting_element.insert(0, value)
		resulting_element.configure(state='readonly')

	def get_possible_temp_states(self):
		return self.temp_types
