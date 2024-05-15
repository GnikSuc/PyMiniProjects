from tkinter import *

#Setting window
my_window = Tk()

#Printig information into cmd about 
print(id(my_window), type(my_window))

width_of_window = 400
height_of_window = 300

screen_width = my_window.winfo_screenwidth()
screen_height = my_window.winfo_screenheight()

window_width = my_window.winfo_reqwidth()
window_height = my_window.winfo_reqheight()

x = (screen_width - width_of_window) // 2
y = (screen_height - height_of_window) // 2

#Title of window
my_window.title("My Window")
my_window.config(bg="#B99E47")
#my_window.configure(width=400,height=300,background="#B99E47")
my_window.geometry(f"{width_of_window}x{height_of_window}+{x}+{y}")
my_window.resizable(width=False, height=False)
my_window.mainloop()

