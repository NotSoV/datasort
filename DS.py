import datetime
import os
global_file_name = ""
results = []
count_extract = []



def program_instructions():
	print("\n   MacLabDataSorter")
	print("  --------------------------------------------------------------------\n")
	print("  Enter name of the log file WITH its .txt extension:")
	user_input = input("  >")
	return user_input

#Work in progress
def make_dir():
	current_directory = os.getcwd()
	final_directory = os.path.join(current_directory, r'Data Files')
	if not os.path.exists(final_directory):
		os.makedirs(final_directory)
   
   
#This will find the lines for user authentication
def find_line_in_file():
	filename = program_instructions()
	textfile = open(filename, 'r')
	matches = []
	for line in textfile:
		if 'checkin: "UserAuthenticate"' in line:
			matches.append(line)
	
	#calling func to retreive a date for custom file name
	date = name_dated_file()
	f=open("ProcessedData_" + date + ".txt", "w+")

	#assigning date name to globvar to be used later
	global global_file_name
	global_file_name = "ProcessedData_" + date + ".txt"
	
	#creating file with processed data
	for i in matches:
		f.write(i)
		
	
	f.close()
	

def name_dated_file():
	time_date = datetime.datetime.now()
	date = str(time_date.month) + "-" + str(time_date.day) + "-" + str(time_date.year)
	return date

		
def find_date_in_file():
	global results
	global count_extract
	count = 0
	with open(global_file_name, 'r') as f:
		contents = f.readlines()
		
		#FOR - to iterate through the months
		for z in range(1,13):
			if z < 10:
				z = "0" + str(z)
			else:
				z = str(z)
			#FOR - to iterate through the days
			for x in range(1,32):
			#IF STATEMENT - to convern iterator to string to 
				if x < 10:
					x = "0" + str(x)
				else:
					x = str(x)
				keyword = "2017/"+ z +"/"+ x
				#FOR - to search line by line for a match to keyword
				for line in contents:	
					if keyword in line:
						count +=1
				results.append(keyword + ": " + str(count))
				count_extract.append(count)
				count = 0
		f.close()	

#CREATE the results file and file it with processed data
def create_results_file():
	date = name_dated_file()
	results_file = open("results_" + date + ".txt", "w+")
	for i in results:
		results_file.write(i + "\n")
	results_file.close()
	print("Creating result file now...")
	
#CREATE the counts file and fill it with count data
def create_a_count_file():
	date = name_dated_file()
	count_file = open("count_" + date + ".txt", "w+")
	for i in count_extract:
		count_file.write(str(i) + "\n")
	count_file.close()
	print("Creating count file now...")

def creat_a_dates_file():
	date = name_dated_file()
	results_file = open("dates_" + date + ".txt", "w+")
	for i in results:
		results_file.write(i[0:len(i)-3] + "\n")
	results_file.close()
	print("Creating dates file now...")



find_line_in_file()
find_date_in_file()

create_results_file()
create_a_count_file()
creat_a_dates_file()

