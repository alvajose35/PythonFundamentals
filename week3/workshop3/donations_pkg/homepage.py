def show_homepage():
	home_page = '''\n	   === DonateMe Homepage ===
------------------------------------------
| 1.   Login       | 2.   Register        |
------------------------------------------
| 3.   Donate      | 4.   Show Donations  |
------------------------------------------
|              5.   Exit                  |
------------------------------------------'''

	print(home_page)

def donate(username):
	
	donation_amt = input("\nEnter amount to donate: ")
	donation_string = f"{username} donated ${donation_amt}"
	print("Thank you for your donation!")

	return donation_string

def show_donations(donations):

	print("\n--- All Donations ---")

	if len(donations) == 0:
		print("Currently, there are no donations.")
	else:
		for don in donations:
			print(don)