from tkinter import *
root = Tk()

monitor_width = root.winfo_screenwidth()
monitor_height = root.winfo_screenheight()

print("width x height = %d x %d (pixels)" % (monitor_width, monitor_height))

width_rat = 2560 / monitor_width
height_rat = 1440 / monitor_height

