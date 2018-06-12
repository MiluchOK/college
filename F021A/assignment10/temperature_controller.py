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

	def convertButtonPressed(self):
		"""
		Python calls this method when the user presses the incrementButton in the View.
		"""
		print('Triggering conversion.')

	def get_possible_temp_states(self):
		return self.temp_types
