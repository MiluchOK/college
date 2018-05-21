"""
The file contains tests for assignment #7 project

Each test is commented with the test description clearly (hopefully) showing what the test does
"""

import unittest
from assignment7 import Employee


class Assignment7Test(unittest.TestCase):

	def setUp(self):
		self.target_first_name = 'John'
		self.target_last_name = 'Doe'
		self.target_ssn = 123123123
		self.target_salary = 10000

		self.target = Employee(self.target_first_name, self.target_last_name, self.target_ssn, self.target_salary)

	"""
	Test checks that Employee can be initialized
	"""

	def test_can_initialize_an_employee(self):
		assert isinstance(self.target, Employee)
		assert self.target.first_name == self.target_first_name
		assert self.target.last_name == self.target_last_name
		assert self.target.ssn == self.target_ssn
		assert self.target.salary == self.target_salary

	"""
	The test checks that user can get a raise
	"""

	def test_can_get_a_raise(self):
		percent_raise = 0.1
		expected_new_salary = self.target.salary + self.target.salary * percent_raise
		self.target.give_raise(percent_raise)
		assert self.target.salary == expected_new_salary



if __name__ == '__main__':
	unittest.main()
