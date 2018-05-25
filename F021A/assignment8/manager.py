from employee import Employee

"""
The class is representing a manager
"""


class Manager(Employee):

	# The constructor (params are self explanatory)
	def __init__(self, first_name, last_name, ssn, salary, title, annual_bonus_amount):
		super().__init__(first_name, last_name, ssn, salary)
		self.title = title
		self.annual_bonus_amount = annual_bonus_amount

	# String representation of the manager object
	def __str__(self):
		original_string = super().__str__()
		return original_string + "\nTitle: {}\nAnnual Bonus: {}".format(self.title, self.annual_bonus_amount)
