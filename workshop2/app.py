# https://replit.com/join/fkymlqecgw-mpac

from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Register User
print("    === Automated Teller Machine ===    ")

while True:
    name = input("Enter name to register: ")
    if len(name) < 1 or len(name) >10:
        print("\nERROR: Name should be between one (1) and ten (10) characters.\n")
        continue
    else:
        break

while True:
    pin = input("Enter PIN: ")
    
    # Validate only numerical input
    try:
        pin = int(pin)
    except ValueError:
        print("\nERROR: PIN should only be numbers.\n")
        continue

    # Validate lenght of PIN
    if len(str(pin)) != 4:
        print("\nERROR: PIN should be four (4) digits.\n")
        continue
    else:
        break
balance = 0
print(name + " has been registred with a starting balance of $" + str(balance) + "\n")


# User login
while True:
    print("    === Automated Teller Machine ===    ")
    user = input("Enter name: ")
    user_PIN = input("Enter PIN: ")

    if user == name and user_PIN == str(pin):
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(user)

    option = input("Choose an option: ")

    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == '3':
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == '4':
        balance = account.logout(user)
        exit()
    else:
        print("Invalid option")

