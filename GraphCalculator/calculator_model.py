from debug import debug
from math import cos, sin, tan, pi

# calculator model variables
calculator_display = '0'
calculator_memory = 0
calculator_graph_range = 300

# calculate what is in the display
def calculate():

	# the global call lets this function change the value of the 
	# variable declared outside of its scope i.e. line 5 for this one
	global calculator_display
	result = 0

	# if the display is not empty then do the calculation 
	if calculator_display.strip() != '':
		debug("calculating: "+calculator_display)

		# use python to evaluate the calculation
		result = eval(calculator_display)

		# update the display variable to store the result
		calculator_display = str(result)
	return result

# adds digits and symbols to the current display
def add_to_display(add_item):
	global calculator_display

	debug("adding: "+str(add_item))
	
	# if the display is a zero then just change it to whats being added, no point in having a leading zero
	if calculator_display.strip() == '0':
		calculator_display = str(add_item)
	# otherwise add it to the end of the display
	else:
		calculator_display += str(add_item)

# if they click the trig buttons then wrap the display in the trig function and add brackets then calculate
def add_trig_display(trig_function):
	global calculator_display

	calculator_display = trig_function+"("+calculator_display+")"
	calculate()

# the following functions just manage the memory feature
def memory_add():
	global calculator_memory
	calculator_memory += calculate()

def memory_substract():
	global calculator_memory
	calculator_memory -= calculate()

def memory_clear():
	global calculator_memory
	calculator_memory = 0

def memory_recall():
	global calculator_display
	global calculator_memory

	calculator_display = str(calculator_memory)

def clear_display():
	global calculator_display
	calculator_display = '0'
