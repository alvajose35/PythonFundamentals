def show_balance(balance):
	print("Current Balance: $" + str(balance))

def deposit(balance):
	amount = float(input("Enter amount to deposit: $"))
	return balance + amount

def withdraw(balance):
	while True:
		amount = float(input("Enter amount to withdraw: $"))

		if amount > balance:
			print("Insufficent funds. Your current balance is: $ " + str(balance))
		else:
			break
	return balance - amount

def logout(name):
	print("Goodbye " + name + "!")