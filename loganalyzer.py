# Loganalyzer 1.0
import sys
print('Log Analyzer 1.0')

def statistics(fileName):
	errors = 0
	notice = 0
	print(f'\nStatistics for {fileName}:\n')
	try:
		with open(fileName, mode='r') as f:
			for line in f:
				if line.find('[error]') != -1:
					errors += 1

				if line.find('[notice]') != -1:
					notice += 1
		print('errors '+str(errors))
		print('notice '+str(notice))
	except FileNotFoundError:
		print(f'Logfile {fileName} not found.')
		return

def error(fileName):
	print(f'\nError summary for {fileName}:\n')
	try:
		with open(fileName, mode='r') as f:
			for line in f:
				if line.find('[error]') != -1:
					dateEnd = line.find(']')
					messageStart = line.find(']', 26)+1
					print(line[1:dateEnd]+line[messageStart:])
	except FileNotFoundError:
		print(f'Logfile {fileName} not found.')
		return

def notice(fileName):
	print(f'\nNotice summary for {fileName}:\n')	
	try:
		with open(fileName, mode='r') as f:
			for line in f:
				if line.find('[notice]') != -1:
					dateEnd = line.find(']')
					messageStart = line.find(']', 26)+1
					print(line[1:dateEnd]+line[messageStart:])
	except FileNotFoundError:
		print(f'Logfile {fileName} not found.')
		return

def availArgs():
	print('Avaliable arguments:')
	print('\tstatistics\t- Show statistics for logfile')
	print('\terror\t\t- Show a summary of error log entries')
	print('\tnotice\t\t- Show a summary of notice log entries')


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print('Missing valid logfile.')
	else:
		fileName = sys.argv[1]
		if len(sys.argv) == 2:
			print('Missing argument.')
			availArgs()
		elif len(sys.argv) == 3:
			argument = sys.argv[2]
			if argument == 'statistics':
				statistics(fileName)
			elif argument == 'error':
				error(fileName)
			elif argument == 'notice':
				notice(fileName)
			else:
				print('\nInvalid argument.')
				availArgs()
		else:
			print('\nInvalid input.')
