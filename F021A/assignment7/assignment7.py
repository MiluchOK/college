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

# Output
"""
First Name: Dory 
Last Name: Groo 
SSN: 631050017
Salary: 403986.0$
Title: QA Manager
Annual Bonus: 9812

First Name: Marry 
Last Name: Boo 
SSN: 894535082
Salary: 72152.3$

First Name: Polly 
Last Name: Groo 
SSN: 730346967
Salary: 739358.4$

First Name: Dory 
Last Name: Foo 
SSN: 360923662
Salary: 279989.6$

First Name: Alex 
Last Name: Mil 
SSN: 643149435
Salary: 650928.3$

First Name: Jane 
Last Name: Voloo 
SSN: 483634834
Salary: 476740.0$
Title: Marketing Manager
Annual Bonus: 3027

First Name: Ana 
Last Name: Sdop 
SSN: 61004088
Salary: 1027798.2$

First Name: Ana 
Last Name: Dinn 
SSN: 505827655
Salary: 292188.6$

First Name: Alex 
Last Name: Foo 
SSN: 171483321
Salary: 969960.2$

First Name: Jane 
Last Name: Mil 
SSN: 10823836
Salary: 717637.8$

First Name: Alex 
Last Name: Boo 
SSN: 327757934
Salary: 50019.2$
Title: Sales Manager
Annual Bonus: 3472

First Name: Simbi 
Last Name: Groo 
SSN: 637414494
Salary: 913657.8$

First Name: Marry 
Last Name: Dinn 
SSN: 650964247
Salary: 967435.7$

First Name: Jane 
Last Name: Sdop 
SSN: 759156566
Salary: 306656.9$

First Name: Simbi 
Last Name: Mil 
SSN: 887158596
Salary: 969612.6$

First Name: Alex 
Last Name: Mil 
SSN: 186819018
Salary: 473193.6$
Title: QA Manager
Annual Bonus: 2352

First Name: Dory 
Last Name: Sdop 
SSN: 656845747
Salary: 661479.5$

First Name: Polly 
Last Name: Foo 
SSN: 413212999
Salary: 1038296.6$

First Name: Dory 
Last Name: Sdop 
SSN: 661217920
Salary: 950824.6$

First Name: Stenley 
Last Name: Foo 
SSN: 853570776
Salary: 506973.5$
"""