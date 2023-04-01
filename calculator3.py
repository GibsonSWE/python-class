print ('Välkommen till Kalkylatorn! Version 3.0\n')


# DEFINING AND RESETTING VARIABLE

ans = ""
operations = ['+', '-', '*', '/']

while True:		
	firstNumber = ""
	secondNumber = ""
	operatorPos = -1
	operator = ""

# INPUT

	inputString = input('Vad vill du beräkna? ').strip().lower()
	
# COMMANDS

	if inputString == 'quit':
		print('Tack för att du använder kalkylatorn!\n')
		break
	elif inputString == 'help':
		print('\nCommands:')
		print('quit = Exit Calculator Application')
		print('ans[operator][number] = Use previous answer in your next calculation\n')
		continue
	else:


# OPERATOR AND NUMBERS CHECK

		if inputString.find('ans') != -1:
			firstNumber = ans
			operatorPos = 3
			operator = inputString[3]

		else:
			for o in operations:
				operatorPos = inputString.find(o)
				if not operatorPos == -1:
					operator = o
					break
				else:
					operator = o

		Numbers = inputString.split(operator)
		if Numbers[0] == 'ans':
			Numbers[0] = str(ans) 


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
		scalculation = int(firstNumber)-int(secondNumber)
	elif operator == '*':
		calculation = int(firstNumber)*int(secondNumber)
	elif operator == '/':
		calculation = int(firstNumber)/int(secondNumber)

	ans = calculation
	print('Svar: '+str(calculation)+'\n')
