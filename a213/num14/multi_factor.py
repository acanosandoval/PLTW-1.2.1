# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "Where were you born"
answer = "Trenton NJ"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
