def fizzbuzz(num):
	for x in range(num):
		if (x+1) % 3 == 0:
			print("Fizz",end='')
		if (x+1) % 5 == 0:
			print("Buzz",end='')
		elif (x+1) % 3 != 0:
			print(x+1,end='')
		print()

fizzbuzz(50)