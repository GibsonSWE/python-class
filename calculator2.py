print ('Välkommen till Kalkylatorn! Version 2.0\n')

while True:


# DEFINING AND RESETTING VARIABLES	
	
	operations = ['+', '-', '*', '/']
	firstNumber = ""
	secondNumber = ""
	operatorPos = -1
	operator = ""

# INPUT

	inputString = input('Vad vill du beräkna? ').strip().lower()
	
# QUIT

	if inputString == 'quit':
		print('Tack för att du använder kalkylatorn!\n')
		break
	else:


# OPERATOR AND NUMBERS CHECK

		for o in operations:
			operatorPos = inputString.find(o)
			if not operatorPos == -1:
				operator = o
				break
			else:
				operator = o

		Numbers = inputString.split(operator)


# INPUT ERROR CHECK

		if operatorPos == -1:
			print('Invalid operator\n')
			continue
		if not Numbers[0].strip().isnumeric():
			print('Invalid first number\n')
			continue
		if not Numbers[1].strip().isnumeric():
			print('Invalid second number\n')
			continue
		if len(Numbers) > 2:
			print('No more than two numbers allowed\n')
			continue


# CALCULATION

	firstNumber = int(Numbers[0])
	secondNumber = int(Numbers[1])

	if operator == '+':
		calculation = int(firstNumber)+int(secondNumber)
	elif operator == '-':
			calculation = int(firstNumber)-int(secondNumber)
	elif operator == '*':
		calculation = int(firstNumber)*int(secondNumber)
	elif operator == '/':
		calculation = int(firstNumber)/int(secondNumber)
	print('Svar: '+str(calculation)+'\n')
