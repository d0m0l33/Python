import sys

from debug import debug
import calculator_console_view
import calculator_gui_view

# main method called when script is executed
def main():

	# test to see if a filename parameter was given to the program

	# if at least 2 arguments given then we are running the program in command line mode
	if len(sys.argv) >= 2:
		debug("Console mode since file was supplied at command line.")
		calculator_console_view.init()
	# otherwise we have no filename argument so we default to GUI mode and init the proper view
	else:
		debug("GUI mode")
		calculator_gui_view.init()

if __name__ == '__main__':
	main()