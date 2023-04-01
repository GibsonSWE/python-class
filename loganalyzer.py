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
		print('    Total Errors: '+str(errors))
		print('    Total Notice: '+str(notice))
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
	print('\nAvaliable arguments:')
	print('\tstatistics\t- Show statistics for logfile')
	print('\terror\t- Show a summary of error log entries')
	print('\tnotice\t- Show a summary of notice log entries')



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
				print('Invalid argument.')
				availArgs()
		else:
			print('Invalid input.')


#The script is used as follows:
#python loganalyzer.py filepath actionwhere
#filepath is the path to the log file to analyze and action is the action required by the script.
#Valid values for the action are statistics, error, notice. 
#The action determines what the script outputs.

#statistics – Prints the statistics as follows:
#errors 340 
#notice 450 
#where the first value is the type of log entry and the second value is the number of such entries there are in the file.

#error – Prints the errors inthe file with each row as follows:
#date message

#notice - Prints the notice in the file with each row as follows:
#date message

#The script reads a logfile in the format seen in the provided sample file test.log.
#Use that file to evaluate your script.