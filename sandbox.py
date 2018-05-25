def asker():
	user_input = input("Please type a real number: ")
	try:
		float(user_input)
	except ValueError:
		print("You typed a char that isn't appropriate in a real number.")
	else:
		print("Thank you for following instructions.")
	finally:
		print("I hope you play again.")
		print("================================ RESTART ================================")
		return asker()


asker()
