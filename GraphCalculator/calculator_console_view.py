import sys
import os
from debug import debug
import calculator_model

def init():
	print("Welcome to the console calculator program view")

	# if we got 2 args then that means we have just the file we read
	if len(sys.argv) == 2:
		debug("reading: "+ sys.argv[1])
		calculate_file(sys.argv[1], None)

	# if we got 3 args then we have a file we can read for calculations and then a file to write results to
	elif len(sys.argv) == 3:
		debug("reading: "+ sys.argv[1])
		debug("writing: "+ sys.argv[2])
		calculate_file(sys.argv[1], sys.argv[2])

	# otherwise the program was called with invalid arguments so print out the usage messages
	else:
		print(usage())

# this function reads the calculations line by line from read_filename and writes them to write_filename
# if it exists.
def calculate_file(read_filename, write_filename):
	
	# check that the file we want to read exists
	if os.path.exists(read_filename):
		debug("read file exists")

		# go through each line
		lines = open(read_filename, 'r')
		for line in lines.readlines():

			# get the line into the calculator model
			calculator_model.calculator_display = line.strip()

			# build the result using the model to do the calculation for us
			result = line.strip()+ " = " + str(calculator_model.calculate())

			# if a write file was provided then write the result to a file otherwise print it out to console
			if write_filename != None:

				debug("writing to file")

				write_file = open(write_filename, "a")
				write_file.write(result+"\n")
				write_file.close()
			else:
				print(result)
	else:
		debug("file does not exists")
		print("Print file does not exist.")
		print(usage())

def usage():
	return "Please provide a file to read calculation lines as the first parameter and a file \
		for writing results to as the second parameter. The second parameter is optional."