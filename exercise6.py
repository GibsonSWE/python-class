print ('Exercise 6\n')

list = []
tuple = ('First Name:', 'Last Name:')
list.append(tuple[0]+' '+tuple[1])

while True:

	inputString = input('Enter Name: ').strip().lower()

	if inputString == 'quit':
		break
	elif inputString == 'printlist':
		print('\nName List:\n')
		for i in list:
			print(i.title())
		print('\n')
		continue
	else:
		list.append(inputString)

