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
NOTE: The more extensive test suit is provided in the unittest file with over 10 test cases
this main is just complimentary to the unit tests.
"""
if __name__ == '__main__':

	# Check that equality works
	e1 = Employee('Alex', 'Mil', 14234, 235235)
	e2 = Manager('Alex', 'Mil', 547567, 56765, 'Some Manager', 435345)
	print("\nIs employee 1: \n{} \nequal to employee 2: \n{}. \n Result: {}".format(e1, e2, e1 == e2))

	# Check the DIRECT comp
	e1 = Employee('Alex', 'Mil', 14234, 235235)
	e2 = Manager('Alex', 'Vil', 547567, 56765, 'Some Manager', 435345)
	print("\nIs employee 1: \n{} \nless than employee 2: \n{}. \n Result: {}".format(e1, e2, e1 < e2))

	# Check the sorting for employees and managers

	company = []
	for i in range(20):
		if i % 5 == 0:
			company.append(EmployeeFactory.generate_manager())
		else:
			company.append(EmployeeFactory.generate_employee())

	print("\nSorted:")
	company = sorted(company)
	for person in company:
		person.give_raise(0.1)
		print("\n" + str(person))

"""
Is employee 1: 
First Name: Alex 
Last Name: Mil 
SSN: 14234
Salary: 235235$ 
equal to employee 2: 
First Name: Alex 
Last Name: Mil 
SSN: 547567
Salary: 56765$
Title: Some Manager
Annual Bonus: 435345. 
 Result: True

Is employee 1: 
First Name: Alex 
Last Name: Mil 
SSN: 14234
Salary: 235235$ 
less than employee 2: 
First Name: Alex 
Last Name: Vil 
SSN: 547567
Salary: 56765$
Title: Some Manager
Annual Bonus: 435345. 
 Result: True

Sorted:

First Name: Jane 
Last Name: Boo 
SSN: 902068163
Salary: 688345.9$

First Name: Dory 
Last Name: Dinn 
SSN: 259084363
Salary: 1062754.0$

First Name: Simbi 
Last Name: Dinn 
SSN: 223613158
Salary: 734652.6$
Title: Eng. Manager
Annual Bonus: 7628

First Name: Alex 
Last Name: Foo 
SSN: 903606195
Salary: 813139.8$

First Name: Alex 
Last Name: Foo 
SSN: 78126982
Salary: 526427.0$

First Name: Dory 
Last Name: Foo 
SSN: 465945703
Salary: 264892.1$

First Name: Polly 
Last Name: Foo 
SSN: 165428729
Salary: 128522.9$

First Name: Alex 
Last Name: Groo 
SSN: 584579258
Salary: 450411.5$

First Name: Dory 
Last Name: Groo 
SSN: 914090188
Salary: 287169.3$

First Name: Simbi 
Last Name: Groo 
SSN: 849276365
Salary: 854439.3$

First Name: Alex 
Last Name: Mil 
SSN: 279217002
Salary: 834023.3$
Title: Eng. Manager
Annual Bonus: 8761

First Name: John 
Last Name: Mil 
SSN: 574507156
Salary: 170358.1$

First Name: Stenley 
Last Name: Mil 
SSN: 279169109
Salary: 134574.0$

First Name: Marry 
Last Name: Sdop 
SSN: 93873330
Salary: 966461.1$

First Name: Alex 
Last Name: Voloo 
SSN: 13815924
Salary: 790731.7$

First Name: Alex 
Last Name: Voloo 
SSN: 421732648
Salary: 593908.7$

First Name: John 
Last Name: Voloo 
SSN: 273061001
Salary: 531975.4$
Title: QA Manager
Annual Bonus: 9975

First Name: Marry 
Last Name: Voloo 
SSN: 115020242
Salary: 385246.4$

First Name: Simbi 
Last Name: Voloo 
SSN: 496372241
Salary: 824797.6$
Title: Eng. Manager
Annual Bonus: 3463

First Name: Simbi 
Last Name: Voloo 
SSN: 872525551
Salary: 52162.0$
"""