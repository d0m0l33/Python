import sys
from math import cos, sin, tan, pi

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

from debug import debug
import calculator_model

# global variables that manage widgets of the calculator
calculator_graph_canvas = None
calculator_display_entry = None
calculator_range_entry = None

# this will update the entry boxes with the data from the calculator_model to make sure they match
# so this is like the controller updating the view and the model to be in synch from model -> view
def update_view():
	global calculator_display_entry
	global calculator_range_entry
	
	# change the value of the display entry box to the value of what is in our model
	calculator_display_entry.set(calculator_model.calculator_display)

	# change the value of the range entry box to the value of what is in our model
	calculator_range_entry.set(str(calculator_model.calculator_graph_range))

# this will update the calculator_model with the data from the entry boxes to make sure they match
# so this is like the controller updating the model and the view to be in synch from view -> model
def update_calculator(*args):
	global calculator_display_entry
	global calculator_range_entry
	
	# the value of the display in the model is assigned the value of the entry box value
	calculator_model.calculator_display = calculator_display_entry.get()

	# now we do the same for the range entry box but we have to make sure its not empty
	if calculator_range_entry.get() != "":

		# convert the value to an integer and assign it to the models range variable
		calculator_model.calculator_graph_range = int(calculator_range_entry.get())

		# then check if that value was less than 10; if so, make it at least 10 because that is the minimum range
		if calculator_model.calculator_graph_range < 10:
			calculator_model.calculator_graph_range = 10

			# call update view to make sure that what is in the model matchs the stuff shown in the view
			update_view()

# init the variables we need to track what the user has entered into the 2 text boxes
def init_app_variables():

	# the main calculation entry box
    global calculator_display_entry
    calculator_display_entry = Tk.StringVar()

	# the range entry box
    global calculator_range_entry
    calculator_range_entry = Tk.StringVar()

	# these two lines attach the 'update_calculator' handler to the event that the user types into
	# any of these 2 entry boxes
    calculator_display_entry.trace('w', update_calculator)
    calculator_range_entry.trace('w', update_calculator)

	# this will make sure that our model has the same data inside it as what is written in the entry box
    update_view()

# this adds the graphing wiget(s) to the root
def init_graphing_widgets(root):
	debug("init graphing widgets")

	# the canvas on which we draw the graph is global so that the draw_graph function can use it to draw the
	# graph later
	global calculator_graph_canvas

	# create a new canvas
	calculator_graph_canvas = Tk.Canvas(root, width=640, height=480, bg = 'white', highlightthickness=0)

	# if the configuration of the canvas change we attach the on_resize handler so that it can handle
	# window resizing the other lines are related to resizing
	calculator_graph_canvas.bind("<Configure>", on_resize)
	calculator_graph_canvas.height = calculator_graph_canvas.winfo_reqheight()
	calculator_graph_canvas.width = calculator_graph_canvas.winfo_reqwidth()
	calculator_graph_canvas.addtag_all("all")

# adds all the calculator buttons and stuff
def init_calculator_widgets(root):
	debug("init calculator widgets")

	# the calculation entry box
	name = Tk.Entry(root, textvariable=calculator_display_entry)
	name.grid(sticky=Tk.E+Tk.W)

	# the range entry box
	name = Tk.Entry(root, textvariable=calculator_range_entry)
	name.grid(sticky=Tk.E+Tk.W)

	# this frame is for all the buttons
	frame = Tk.Frame(root)

	# digit buttons
	btn = Tk.Button(master=frame, text='7', command=lambda: [calculator_model.add_to_display(7), update_view()])
	btn.grid(row = 1, column = 1)
	btn = Tk.Button(master=frame, text='8', command=lambda: [calculator_model.add_to_display(8), update_view()])
	btn.grid(row = 1, column = 2)
	btn = Tk.Button(master=frame, text='9', command=lambda: [calculator_model.add_to_display(9), update_view()])
	btn.grid(row = 1, column = 3)
	btn = Tk.Button(master=frame, text='4', command=lambda: [calculator_model.add_to_display(4), update_view()])
	btn.grid(row = 2, column = 1)
	btn = Tk.Button(master=frame, text='5', command=lambda: [calculator_model.add_to_display(5), update_view()])
	btn.grid(row = 2, column = 2)
	btn = Tk.Button(master=frame, text='6', command=lambda: [calculator_model.add_to_display(6), update_view()])
	btn.grid(row = 2, column = 3)
	btn = Tk.Button(master=frame, text='1', command=lambda: [calculator_model.add_to_display(1), update_view()])
	btn.grid(row = 3, column = 1)
	btn = Tk.Button(master=frame, text='2', command=lambda: [calculator_model.add_to_display(2), update_view()])
	btn.grid(row = 3, column = 2)
	btn = Tk.Button(master=frame, text='3', command=lambda: [calculator_model.add_to_display(3), update_view()])
	btn.grid(row = 3, column = 3)
	btn = Tk.Button(master=frame, text='0', command=lambda: [calculator_model.add_to_display(0), update_view()])
	btn.grid(row = 4, column = 1, columnspan=2, sticky=Tk.E+Tk.W)

	# . button
	btn = Tk.Button(master=frame, text=".", command=lambda: [calculator_model.add_to_display('.'), update_view()])
	btn.grid(row = 4, column = 3)

	# trig buttons
	btn = Tk.Button(master=frame, text='sin', command=lambda: [calculator_model.add_trig_display('sin'), update_view()])
	btn.grid(row = 1, column=5)
	btn = Tk.Button(master=frame, text='cos', command=lambda: [calculator_model.add_trig_display('cos'), update_view()])
	btn.grid(row = 2, column=5)
	btn = Tk.Button(master=frame, text='tan', command=lambda: [calculator_model.add_trig_display('tan'), update_view()])
	btn.grid(row = 3, column=5)
	btn = Tk.Button(master=frame, text='PI', command=lambda: [calculator_model.add_to_display('pi'), update_view()])
	btn.grid(row = 4, column=5)

	# operator buttons
	btn = Tk.Button(master=frame, text='/', command=lambda: [calculator_model.add_to_display('/'), update_view()])
	btn.grid(row = 1, column=6)
	btn = Tk.Button(master=frame, text='x', command=lambda: [calculator_model.add_to_display('*'), update_view()])
	btn.grid(row = 2, column=6)
	btn = Tk.Button(master=frame, text='-', command=lambda: [calculator_model.add_to_display('-'), update_view()])
	btn.grid(row = 3, column=6)
	btn = Tk.Button(master=frame, text='+', command=lambda: [calculator_model.add_to_display('+'), update_view()])
	btn.grid(row = 4, column=6)

	# memory buttons
	btn = Tk.Button(master=frame, text='mr', command=lambda: [calculator_model.memory_recall(), update_view()])
	btn.grid(row = 1, column=7)
	btn = Tk.Button(master=frame, text='mc', command=lambda: [calculator_model.memory_clear(), update_view()])
	btn.grid(row = 2, column=7)
	btn = Tk.Button(master=frame, text='m-', command=lambda: [calculator_model.memory_substract(), update_view()])
	btn.grid(row = 3, column=7)
	btn = Tk.Button(master=frame, text='m+', command=lambda: [calculator_model.memory_add(), update_view()])
	btn.grid(row = 4, column=7)

	# calcualte button
	btn = Tk.Button(master=frame, text='Calculate', command=lambda: [calculator_model.calculate(), update_view()])
	btn.grid(row = 1, rowspan=1, column=8, columnspan=2, sticky=Tk.N+Tk.E+Tk.S+Tk.W)

	# graph button
	btn = Tk.Button(master=frame, text='Graph', command=lambda:draw_graph())
	btn.grid(row = 1, rowspan=1, column=10, columnspan=2, sticky=Tk.N+Tk.E+Tk.S+Tk.W)

	# clear button
	btn = Tk.Button(master=frame, text='CLEAR', command=lambda:[calculator_model.clear_display(), update_view()])
	btn.grid(row = 2, rowspan=1, column=8, columnspan=2, sticky=Tk.N+Tk.E+Tk.S+Tk.W)

	# make the frame stretch to the cell
	frame.grid(sticky=Tk.N+Tk.E+Tk.S+Tk.W)

# this handler scales the graph if the window is resized
def on_resize(event):
	debug("resizing")

	global calculator_graph_canvas

	# determine the ratio of old width/height to new width/height
	wscale = float(event.width)/calculator_graph_canvas.width
	hscale = float(event.height)/calculator_graph_canvas.height

	calculator_graph_canvas.width = event.width
	calculator_graph_canvas.height = event.height
	# resize the canvas
	calculator_graph_canvas.config(width=calculator_graph_canvas.width, height=calculator_graph_canvas.height)
	# rescale all the objects tagged with the "all" tag
	calculator_graph_canvas.scale("all",0,0,wscale,hscale)

# this will draw a graph onto the canvas
def draw_graph():
	debug("graphing contents of calculator entry")

	# get the global canvas
	canvas = calculator_graph_canvas

	# clear whatever it already has
	canvas.delete('all')

	# put it into the grid of the widget
	canvas.grid(sticky=Tk.N+Tk.E+Tk.S+Tk.W)
	
	# get the current height and width
	h = canvas.height
	w = canvas.width

	# find the center
	centerx = w/2
	centery = h/2

	# determine the range we need to use, this comes from our calculator model
	user_range = calculator_model.calculator_graph_range

	# determine if we need to scale
	scaling = (w/2)/user_range

	# draw the x axis and draw the y axis
	canvas.create_line(0,centery,w,centery, width=1) 
	canvas.create_line(centerx,0,centerx,h, width=1)
	
	# draw the ticks and the number beside each tick for the x-axis
	alternate = 0
	for i in range(int(w/2/10)): 

		# x of ticks going towards the right from the center
		x = centerx + (i*10)

		# x of ticks going towards the left from the center
		x_neg = centerx - (i*10)

		# create the tick lines for both sides
		canvas.create_line(x,h/2,x,(h/2)+5, width=1)
		canvas.create_line(x_neg,h/2,x_neg,(h/2)+5, width=1)

		# alternate basically counts every 3rd tick and puts a number there, because we cant fit a number
		# at every tick
		if(alternate == 2):
			# note here that the number drawn is dependant on the value of scaling this is how it shows
			# the range the user wants
			canvas.create_text(x,(h/2)+5, text='%d'% ((10*i)/scaling), anchor=Tk.N)
			canvas.create_text(x_neg,(h/2)+5, text='%d'% ((10*i)/scaling), anchor=Tk.N)
		alternate = (1+ alternate) % 3
	
	# reset alternate
	alternate = 0

	# do the same thing as above for the y-axis ticks
	for i in range(int(h/2/10)): 
		y = centery + (i * 10)
		y_neg = centery - (i*10)

		canvas.create_line(w/2,y,(w/2)+5,y, width=1)
		canvas.create_line(w/2,y_neg,(w/2)+5,y_neg, width=1)
		
		if(alternate == 2):
			canvas.create_text((w/2)-5,y, text='%d'% ((10*i)/scaling), anchor=Tk.E)
			canvas.create_text((w/2)-5,y_neg, text='%d'% ((10*i)/scaling), anchor=Tk.E)
		alternate = (1+ alternate) % 3
	
	# create two empty lists that will countain our plotting data
	scaled = []
	coords = []
	
	# get the function that is currently in the model's display
	func = calculator_model.calculator_display

	# if there is a function and its not empty
	if func != None and func != "":

		# go from the maximum negative to the maximum positive based on the size of the canvas width
		for x in range(int(-(w*10/2)), int((w*10/2))):
			x = x/10.0
			# for each of these x's calculate the y and convert to integer
			calculated_y = eval(func)

			if calculated_y > h/2 or calculated_y < (-h/2):
				pass
			else:
				coords.append((x, calculated_y))
		
		debug(coords)

		# now go through all these coordinate and scale them based on the range the user has chosen		
		for (x,y) in coords:

			# its important to see that we have to calculate the new coordinates based on scale and the center
			# position being in the center of the canvas not at 0,0 which is in the top left of the canvas
			scaled.append((centerx+(x*scaling), centery-(y*scaling)))

		# create a line that goes through all these points
		canvas.create_line(scaled, fill='royalblue', smooth=1)

	# this tags all the elements in the canvas in the "all" tag so that we can scale them when the window
	# is resized (see on_resize handler)
	canvas.addtag_all("all")

# init the tkinter gui
def init():
	root = Tk.Tk()
	root.wm_title("Scientific Calculator")
	
	# these 2 lines allow for resizing
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)

	# init all the variables i need for the gui
	init_app_variables()

	# init all the widgets i need for graphing
	init_graphing_widgets(root)

	# draw the graph based on the current value of the calculator display
	draw_graph()

	# init all the widgets i need for using calculator features
	init_calculator_widgets(root)

	# start the gui program
	Tk.mainloop()