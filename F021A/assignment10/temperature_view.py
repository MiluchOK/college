from tkinter import *


class TemperatureView(Frame):
	"""
	class MyFrame is the VIEW for a simple program that exemplifies the Model/View/Controller architecture. This View class is a tkinter.Frame that contains two Buttons and a Label. One Button increments a counter and the other Button quits. The Label displays the current value of the counter. Notice that the View never contains a reference to the Model, but it does contain a reference to the Controller.
	"""

	def __init__(self, controller):
		Frame.__init__(self)
		self.pack()
		self.controller = controller

		temperature_types = self.controller.get_possible_temp_states()

		# Temperature conversion type
		self.selected_temp_state = StringVar()
		self.selected_temp_state.set(temperature_types[0])
		self.temp_states = OptionMenu(self, self.selected_temp_state, *temperature_types)
		self.temp_states.pack({"side": "left"})

		# The input field
		self.temperature_value_input = Entry(self)
		self.temperature_value_input.pack({"side": "left"})

		# Conversion button
		self.convertButton = Button(self)
		self.convertButton["text"] = "Convert"
		self.convertButton["command"] = self.controller.convertButtonPressed()
		self.convertButton.pack(side=BOTTOM)

		# Quit button
		self.quitButton = Button(self)
		self.quitButton["text"] = "Quit"
		self.quitButton["command"] = self.quit
		self.quitButton.pack(side=BOTTOM)

		# Start the view
		self.mainloop()
