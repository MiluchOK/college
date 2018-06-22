""" One object of class Account represents one bank account """


class Account:
	def __init__(self):
		print("Account constructor")
		self.balance = 0
		self.customer = "Mickey Mouse"

	def deposit(self, amount):
		self.balance = self.balance + amount

	def __str__(self):
		return "%s has a balance of %d" % (self.customer, self.balance)

	def __int__(self):
		"""
		The method returns int representation of the object
		:return: int
		"""
		return self.balance


class SavingsAccount(Account):
	# syntax above shows that SavingsAccount is a subclass of the superclass Account

	def __init__(self):
		Account.__init__(self)  # calls the Account constructor to initialize that part of the object
		print("SavingsAccount constructor")
		self.interestRate = 0.05

	def __str__(self):
		return Account.__str__(self) + ", and the interest rate is " + str(self.interestRate)


account = SavingsAccount()
account.__int__()
