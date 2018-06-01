"""
The file contains tests for assignment #7 project

Each test is commented with the test description clearly (hopefully) showing what the test does
"""

import unittest
from employee import Employee
from manager import Manager


class Assignment8Test(unittest.TestCase):

	def setUp(self):
		self.target_first_name = 'John'
		self.target_last_name = 'Doe'
		self.target_ssn = 123123123
		self.target_salary = 10000

		# Init an employee
		self.target = Employee(self.target_first_name, self.target_last_name, self.target_ssn, self.target_salary)

		self.target_manager_first_name = 'Jane'
		self.target_manager_last_name = 'Doe'
		self.target_manager_ssn = 666666666
		self.target_manager_salary = 99999
		self.target_manager_title = 'Eng Manager'
		self.target_manager_annual_bonus_amount = 6666

		# Init a manager
		self.target_manager = Manager(
			self.target_manager_first_name,
			self.target_manager_last_name,
			self.target_manager_ssn,
			self.target_manager_salary,
			self.target_manager_title,
			self.target_manager_annual_bonus_amount
		)

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
	The test checks that user can give a raise to an employee
	"""

	def test_can_get_a_raise(self):
		percent_raise = 0.1
		expected_new_salary = self.target.salary + self.target.salary * percent_raise
		self.target.give_raise(percent_raise)
		assert self.target.salary == expected_new_salary

	"""
	The test checks that user can initialize a manager
	"""

	def test_can_initialize_a_manager(self):
		assert isinstance(self.target_manager, Manager)
		assert self.target_manager.first_name == self.target_manager_first_name
		assert self.target_manager.last_name == self.target_manager_last_name
		assert self.target_manager.title == self.target_manager_title
		assert self.target_manager.annual_bonus_amount == self.target_manager_annual_bonus_amount
		assert self.target_manager.ssn == self.target_manager_ssn
		assert self.target_manager.salary == self.target_manager_salary

	"""
	The test checks that manager can get a raise
	"""

	def test_manager_can_get_a_raise(self):
		percent_raise = 0.1
		expected_new_salary = self.target_manager.salary + self.target_manager_salary * percent_raise
		self.target_manager.give_raise(percent_raise)
		assert self.target_manager.salary == expected_new_salary

	"""
	The test checks that employees can be equal
	"""

	def test_employee_can_be_equal(self):
		other_employee = Employee(self.target_first_name, self.target_last_name, self.target_ssn, self.target_salary)
		assert self.target == other_employee, True

	"""
		The test checks that employees are not always equal
	"""

	def test_employee_not_always_equal(self):
		other_employee = Employee("Fooo", "Booo", 111111111, 2342353)
		self.assertFalse(self.target == other_employee)

	"""
	The test checks that managers can be equal
	"""

	def test_managers_can_be_equal(self):
		other_manager = Manager(self.target_manager_first_name,
								 self.target_manager_last_name,
								 self.target_manager_ssn,
								 self.target_manager_salary,
								 self.target_manager_title,
								 self.target_manager_annual_bonus_amount)
		assert self.target_manager == other_manager, True

	"""
		The test checks that managers are not always equal
	"""

	def test_managers_not_always_equal(self):
		other_manager = Manager("Foo", "Boo", 111111111, 23234, "QA Manager", 325234)
		self.assertFalse(self.target_manager == other_manager)


if __name__ == '__main__':
	unittest.main()
