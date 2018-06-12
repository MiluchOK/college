import tkinter

import temperature_view
import temperature_controller

if __name__ == "__main__":
    c = temperature_view.TemperatureView(temperature_controller.TemperatureController())