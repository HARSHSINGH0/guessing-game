import random
randomnumber=random.randrange(1,100)
user_input=None
while user_input != randomnumber:
	user_input=int(input("enter number:"))
	if (user_input < randomnumber):
		print("entered number is less ")
	elif (user_input > randomnumber):
		print("entered number is more")
	else:
		print("correct:",randomnumber)
