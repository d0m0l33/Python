# toggle this to True or False to enable debug messages when we run the program
debug_flag = True

# this method is used by the other files to output debug messages to console
def debug(msg):
	if debug_flag:
		print(":::DEBUG:", msg)