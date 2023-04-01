print ('Välkommen till Kalkylatorn! Version 1.0\n')

while True:
	
	operations = ['+', '-', '*', '/']
	first_number = ""
	second_number = ""
	operator_pos = 0
	operator = ""
	next_number_flag = False
	calc_str = input('Vad vill du beräkna? ').strip().lower()
	
	if calc_str == 'quit':
		print('Tack för att du använder kalkylatorn!\n')
		break
	else:
		for o in operations:
			operator_pos = calc_str.find(o)
			if operator_pos != -1:
				operator = o
				break

		for i in calc_str:
			if i.isnumeric() == True and next_number_flag == False:
				first_number = first_number + i
			elif i.isnumeric() == False:
				next_number_flag = True	
			elif i.isnumeric() == True and next_number_flag == True:
				second_number = second_number + i

	if len(first_number) == 0:
		print('Du måste ange två tal samt en operator.\n')
	elif operator != '+' and operator != '-' and operator != '*' and operator != '/':
		print('Du måste ange en giltig operator.\n')
	elif len(second_number) == 0:
		print('Du måste ange två tal.\n')
	else:		
		if operator == '+':
			calculation = int(first_number)+int(second_number)
		elif operator == '-':
			calculation = int(first_number)-int(second_number)
		elif operator == '*':
			calculation = int(first_number)*int(second_number)
		elif operator == '/':
			calculation = int(first_number)/int(second_number)
		print('Svar: '+str(calculation)+'\n')

