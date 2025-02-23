class User:
	def __init__(self, name, pin, password):
		self.name = name
		self.pin = pin
		self.password = password

	def change_name(self, new_name):
		if len(new_name) < 2 or len(new_name) > 10 or self.name == new_name or " " in new_name:
			print("ERROR: New name must differ from original and should be between 2 and 10 characters long (no spaces).")
			return
		self.name = new_name

	def change_pin(self, new_pin):
		if len(str(new_pin)) != 4 or new_pin == self.pin:
			print("ERROR: PIN must differ from original and should be 4 digits.")
			return
		self.pin = new_pin

	def change_password(self, new_password):
		if len(new_password) < 5 or new_password == self.password or " " in new_password:
			print("ERROR: Password must differ from original and should be at least 5 characters long (no spaces).")
			return
		self.password = new_password

class BankUser(User):
	def __init__(self, name, pin, password):
		super().__init__(name, pin, password)
		self.balance = 0
		self.on_hold = False

	def show_balance(self):
		print(f"{self.name} has an account balance of: ${self.balance:.2f}")

	def withdraw(self, amount):
		if amount < 0:
			print("ERROR: Can only withdraw positive amounts.")
			return
		
		if self.on_hold:
			print("ERROR: Your account is currently On-Hold.")
			return

		self.balance -=	amount
		
	def deposit(self, amount):
		if amount < 0:
			print("ERROR: Can only deposit positive amounts.")
			return

		if self.on_hold:
			print("ERROR: Your account is currently On-Hold.")
			return

		self.balance +=	amount

	def transfer_money(self, recipient, amount):
		print(f"\nYou are transfering ${amount} to {recipient.name}")
		
		if amount < 0:
			print("ERROR: Can only transfer positive amounts.")
			return
		
		if amount > self.balance:
			print(f"ERROR: Transfer amount (${amount}) is greater than your current balance (${self.balance}).")
			return
		
		if self.on_hold or recipient.on_hold:
			print("ERROR: An account is currently On-Hold.")
			return
		
		print("Authentication Required")
		transfer_pin = int(input("Enter your PIN: "))
		if transfer_pin != self.pin:
			print("Invalid PIN. Transaction canceled.")
			return False
		
		print("Transfer Authorized")
		print(f"Transfering ${amount} to {recipient.name}")

		self.withdraw(amount)
		recipient.deposit(amount)
		return True
	
	def request_money(self, sender, amount):
		print(f"\nYou are requesting ${amount} from {sender.name}")
		
		if amount < 0:
			print("ERROR: Can only request positive amounts.")
			return

		if amount > sender.balance:
			print(f"ERROR: Request amount (${amount}) is greater than {sender.name}'s current balance (${self.balance}).")
			return

		if sender.on_hold or self.on_hold:
			print("ERROR: An account is currently On-Hold.")
			return
		
		print("User Authentication Required...")
		sender_entered_pin = int(input(f"Enter {sender.name} PIN: "))

		if sender_entered_pin != sender.pin:
			print("Invalid PIN. Transaction canceled.")
			return False
		
		user_password = input("Enter your password: ")
		if user_password != self.password:
			print("Invalid password. Transaction canceled.")
			return False
		

		print("Request authorized")
		print(f"{sender.name} sent ${amount}")
		
		sender.withdraw(amount)
		self.deposit(amount)

		return True
	
	def flip_hold(self):
		self.on_hold = not self.on_hold
		return self.on_hold


# Driver Code for Task 1
'''print("Driver Code for Task 1")
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)'''

# Driver Code for Task 2
'''print("Driver Code for Task 2")
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
user1.change_name("Bobby")
user1.change_pin(4321)
user1.change_password("newpassword")
print(user1.name, user1.pin, user1.password)'''

# Driver Code for Task 3
'''print("Driver Code for Task 3")
user1 = BankUser("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password, user1.balance)'''

# Driver Code for Task 4
'''print("Driver Code for Task 4")
user1 = BankUser("Bob", 1234, "password")
user1.show_balance()
user1.deposit(1000)
user1.show_balance()
user1.withdraw(500)
user1.show_balance()'''

# Driver Code for Task 5
'''print("Driver Code for Task 5")
user1 = BankUser("Bob", 1234, "bobpassword")
user2 = BankUser("Alice", 5678, "alicepassword")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
successful_transfer = user2.transfer_money(user1, 500)
user2.show_balance()
user1.show_balance()
if successful_transfer:
	user2.request_money(user1, 250)
	user2.show_balance()
	user1.show_balance()'''

# Driver Code for Bonus 1
'''print("Driver Code for Bonus 1")
user1 = BankUser("Bob", 1234, "bobpassword")
user2 = BankUser("Alice", 5678, "alicepassword")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
user2.deposit(-500)
user2.withdraw(-500)
successful_transfer = user2.transfer_money(user1, -500)
successful_transfer = user2.transfer_money(user1, 500)
user2.show_balance()
user1.show_balance()
if successful_transfer:
	user2.request_money(user1, -250)'''

# Driver Code for Bonus 2
'''print("Driver Code for Bonus 2")
user1 = BankUser("Bob", 1234, "bobpassword")
user2 = BankUser("Alice", 5678, "alicepassword")
user1.deposit(500)
user2.deposit(500)
user1.show_balance()
user2.show_balance()
user2.transfer_money(user1, 1000)
user2.request_money(user1, 1000)
user1.show_balance()
user2.show_balance()'''

# Driver Code for Bonus 3
'''print("Driver Code for Bonus 3")
user1 = BankUser("Bob", 1234, "bobpassword")
user1.change_name("H")
user1.change_name("Hazsxdfghjklsdfghjklsdfghjkl")
user1.change_name("Bob")
user1.change_name("Bobby Brown")
user1.change_name("Bobby")
user1.change_password("pa")
user1.change_password("bobpassword")
user1.change_password("pass word")
user1.change_password("bobnewpassword")
user1.change_pin(1)
user1.change_pin(12345)
user1.change_pin(1234)
user1.change_pin(5678)
print(user1.name, user1.password, user1.pin)'''

# Driver Code for Bonus 4
'''print("Driver Code for Bonus 4")
user1 = BankUser("Bob", 1234, "bobpassword")
user1.deposit(5000)
user1.show_balance()'''

# Driver Code for Bonus 5
print("Driver Code for Bonus 5")
user1 = BankUser("Bob", 1234, "bobpassword")
user2 = BankUser("Alice", 5678, "alicepassword")
user2.deposit(5000)
user1.deposit(5000)
user2.flip_hold()
user2.deposit(500)
user2.withdraw(500)
user2.transfer_money(user1, 500)
user2.request_money(user1, 250)
user2.flip_hold()
user1.flip_hold()
user2.transfer_money(user1, 500)
user2.request_money(user1, 250)
user1.flip_hold()
user2.deposit(500)
user2.withdraw(500)
user2.transfer_money(user1, 500)
user2.request_money(user1, 250)
