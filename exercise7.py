print ('Exercise 7')

userData = {}

while True:

	inputString = input('Enter full name and salary: ').strip().lower()
	inputList = inputString.split(' ')

	if inputString == 'quit':
		break
	elif inputString == 'printdata' or inputString == 'pd':
		print('\n')
		print('First Name:	Second Name:	Salary:')

		for user in userData:
			print(userData[user][0].title()+'\t\t'+userData[user][1].title()+'\t\t'+userData[user][2])
		print('\n')

	elif len(inputList) < 3 or not inputList[2].isnumeric() or inputList[0].isnumeric() or inputList[1].isnumeric():
		print('Invalid input')
		continue

	else:
		nextUserID = len(userData)+1
		userData[nextUserID] = inputList