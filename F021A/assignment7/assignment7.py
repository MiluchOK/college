"""
The program builds multiple employees and managers and outputs it's properties
"""

"""
The class is a representation of an Employee
"""

class Employee():

	def __init__(self, first_name, last_name, ssn, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.ssn = ssn
		self.salary = salary

	def give_raise(self, percent_raise):
		self.salary += self.salary * percent_raise

	def __str__(self):
		return "First Name: {} \nLast Name: {} \nSSN: {}\nSalary: {}"\
			.format(self.first_name, self.last_name, self.ssn, self.salary)

