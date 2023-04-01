# Loganalyzer 1.0
print('Log Analyzer 1.0')
import sys

def statistics(fileName):
	errors = 0
	notice = 0
	print('\nStatistics for '+fileName+':')
	with open(fileName, mode='r') as f:

		for line in f:
			if line.find('[error]') != -1:
				errors += 1

			if line.find('[notice]') != -1:
				notice += 1
	print('    Total Errors: '+str(errors))
	print('    Total Notice: '+str(notice))

def error(fileName):
	print('\nError summary for '+fileName+':\n')
	with open(fileName, mode='r') as f:
		for line in f:
			if line.find('[error]') != -1:
				dateEnd = line.find(']')+1
				messageStart = line.find(']', 26)+1
				print(line[0:dateEnd]+line[messageStart:])

def notice(fileName):
	print('\nNotice summary for '+fileName+':\n')
	with open(fileName, mode='r') as f:
		for line in f:
			if line.find('[notice]') != -1:
				dateEnd = line.find(']')+1
				messageStart = line.find(']', 26)+1
				print(line[0:dateEnd]+line[messageStart:])

def availArgs():
	print('\nAvaliable arguments:')
	print('\t[s]tats\t\t- Show statistics for logfile')
	print('\t[e]rror\t\t- Show a summary of error log entries')
	print('\t[n]otice\t- Show a summary of notice log entries')



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
			if argument == 'stats' or argument == 's':
				statistics(fileName)
			elif argument == 'error' or argument == 'e':
				error(fileName)
			elif argument == 'notice' or argument == 'n':
				notice(fileName)
			else:
				print('Invalid argument.')
				availArgs()
		else:
			print('Invalid input')


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