"""Main file."""

###############################################
# RANDOM PASSWORD GENERATOR [v0.4 23-03-2023] #
###############################################

#Import necessary modules
import tkinter as tk
from app import PasswordGeneratorApp

#Create and run the application
root = tk.Tk()
app = PasswordGeneratorApp(master=root, width=600, height=370)
app.mainloop()