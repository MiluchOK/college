"""
The class is a representation of an Employee
"""


class Employee():

	# The constructor (param are self explanatory)
	def __init__(self, first_name, last_name, ssn, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.ssn = ssn
		self.salary = salary

	# Give the employee a raise as the percentage supplied as the param
	def give_raise(self, percent_raise):
		self.salary += self.salary * percent_raise

	# Check if employees are equal
	def __eq__(self, other):
		if self.first_name.lower() == other.first_name.lower() and \
				self.last_name.lower() == other.last_name.lower():
			return True
		else:
			return False

	# Compare employees
	def __lt__(self, other):
		self_name = self.last_name + self.first_name
		other_name = other.last_name + other.first_name
		if self_name.lower() < other_name.lower():
			return True
		else:
			return False

	# Return the string representation of the employee
	def __str__(self):
		return "First Name: {} \nLast Name: {} \nSSN: {}\nSalary: {}$" \
			.format(self.first_name, self.last_name, self.ssn, self.salary)
