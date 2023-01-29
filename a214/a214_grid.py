#   a214_grid.py
import tkinter as tk

#main window
root = tk.Tk()
root.wm_geometry("300x300")
root.title("Grid")

#BLUE FRAME
blue_frame = tk.Frame(root, background='blue', width=200, height=150)
blue_frame.grid(row=0, column=0)

#GREEN FRAME
green_frame = tk.Frame(root, background='green', width=100, height=150)
green_frame.grid(row=0, column=1)

#RED FRAME
red_frame = tk.Frame(root, background='red', width=200, height=150)
red_frame.grid(row=1, column=0)

#YELLOW FRAME
red_frame = tk.Frame(root, background='yellow', width=100, height=150)
red_frame.grid(row=1, column=1)

root.mainloop()