import random

"""
The program builds multiple employees and managers and outputs it's properties
"""

from employee import Employee
from manager import Manager

"""
Generate random ssn number
"""


def get_random_ssn():
	return random.randint(000000000, 999999999)


"""
Generate random salary
"""


def get_random_salary():
	return random.randint(1111, 999999)


"""
Generate random first name
"""


def get_random_first_name():
	options = ['Alex', 'John', 'Jane', 'Ana', 'Marry', 'Simbi', 'Dory', 'Polly', 'Stenley']
	return random.choice(options)


"""
Generate random last name
"""


def get_random_last_name():
	options = ['Mil', 'Dinn', 'Foo', 'Boo', 'Groo', 'Voloo', 'Sdop']
	return random.choice(options)


"""
Generate random title
"""


def get_random_title():
	base_title = 'Manager'
	options = ['QA', 'Eng.', 'Marketing', 'Infrastructure', 'Sales', 'HR']
	return "{} {}".format(random.choice(options), base_title)


"""
Generate random annual bonus
"""


def get_random_annual_bonus_amount():
	return random.randint(1111, 9999)


"""
The class is for generation of new Employees and it's derivatives
"""


class EmployeeFactory():
	"""
	Generate an employee object with random data
	"""

	@staticmethod
	def generate_employee():
		return Employee(get_random_first_name(), get_random_last_name(),
						get_random_ssn(), get_random_salary())

	"""
	Generate a manager object with random data
	"""

	@staticmethod
	def generate_manager():
		return Manager(get_random_first_name(), get_random_last_name(),
					   get_random_ssn(), get_random_salary(),
					   get_random_title(), get_random_annual_bonus_amount())


"""
The main will generate a list of employees and manges and then iterate over the list to print out the details
about each one 
"""
if __name__ == '__main__':
	company = []
	for i in range(20):
		if i % 5 == 0:
			company.append(EmployeeFactory.generate_manager())
		else:
			company.append(EmployeeFactory.generate_employee())

	for person in company:
		person.give_raise(0.1)
		print("\n" + str(person))
