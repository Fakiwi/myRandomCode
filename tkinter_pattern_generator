import tkinter as tk
import random

def make_widget():
	choice = random.randint(0,3)
	background = ''
	if choice == 0:
		choice = 'left'
		background = 'light blue'
	elif choice == 1:
		choice = 'top'
		background = 'light green'
	elif choice == 2:
		choice = 'right'
		background = 'yellow'
	elif choice == 3:
		choice = 'bottom'
		background = 'pink'
	final_cmd = 'tk.Label(win, text="'
	final_cmd += choice 
	final_cmd += '", bg="'
	final_cmd += background
	final_cmd += '").pack(side = tk.'
	final_cmd += choice.upper()
	final_cmd += ')'
	exec(final_cmd)
	

def make_ten_widget():
	for i in range(10):
		make_widget()


win = tk.Tk()

button = tk.Button(win, text="Create Random Widget", command=make_widget)
button.pack()

button_ten = tk.Button(win, text="Create 10 Random Widgets", command=make_ten_widget)
button_ten.pack()

win.mainloop()


