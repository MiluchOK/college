from tkinter import *


class TemperatureView(Frame):
	"""
	class MyFrame is the VIEW for a simple program that exemplifies the Model/View/Controller architecture. This View class is a tkinter.Frame that contains two Buttons and a Label. One Button increments a counter and the other Button quits. The Label displays the current value of the counter. Notice that the View never contains a reference to the Model, but it does contain a reference to the Controller.
	"""

	def __init__(self, controller):
		Frame.__init__(self)
		self.pack()
		self.controller = controller

		# Temperature conversion type selector #1
		self.firstTemperatureState = self.buildTemperatureTypeSelector(self)

		# User Input field
		self.temperature_value_input = Entry(self)
		self.temperature_value_input.pack({"side": "left"})

		# Temperature conversion type selector #2
		self.secondTemperatureState = self.buildTemperatureTypeSelector(self)

		# The resulting value
		self.convertedTemperature = Entry(self, state='disabled')
		self.convertedTemperature.pack({"side": "left"})

		# Conversion button
		self.convertButton = Button(self)
		self.convertButton["text"] = "Convert"
		self.convertButton["command"] = lambda: self.controller.convertButtonPressed(
			self.temperature_value_input.get(),
			self.firstTemperatureState.get(),
			self.secondTemperatureState.get(),
			self.convertedTemperature
		)
		self.convertButton.pack(side=BOTTOM)

		# Quit button
		self.quitButton = Button(self)
		self.quitButton["text"] = "Quit"
		self.quitButton["command"] = self.quit
		self.quitButton.pack(side=BOTTOM)

		# Start the view
		self.mainloop()

	def buildTemperatureTypeSelector(self, frame):
		"""
		Generate a selector for temperature type
		:param frame:
		:return:
		"""
		temperature_types = self.controller.get_possible_temp_states()
		selected_temp_state = StringVar()
		selected_temp_state.set(temperature_types[0])
		temp_states = OptionMenu(frame, selected_temp_state, *temperature_types)
		temp_states.pack({"side": "left"})
		return selected_temp_state
