# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

ent_user = input("Enter your username: " )
if (len(ent_user)<8) or (len(ent_user)>24):
    print("Invalid username; must be 8-24 characters long.")
    ent_user = input("Enter a new username: " )
else:
    print("good username")

while not ent_user.isdigit():
    print("Invalid username; must include both letters and numbers.")
    ent_user = input("Enter a new username: " )

ent_password = input("Enter your password: " )

# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

my_auth.set_authorization(ent_user,ent_password)
# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()