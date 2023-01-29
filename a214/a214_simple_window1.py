#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

#button testing func
def test_my_button():
    frame_auth.tkraise()
    password_display = ent_password.get()
    lbl_password_show.config(text=password_display)

#main window
root = tk.Tk()
root.wm_geometry("200x160")
root.title("Authorization")

#LOGIN FRAME
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

#username label
lbl_username = tk.Label(frame_login, text='Username:',font="Courier")
lbl_username.pack()
#username entry box
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

#password label
lbl_password = tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack()
#password entry box
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

#login button
btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack(pady=5)



#AUTHORIZATION FRAME
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

#password shown label
lbl_password_show = tk.Label(frame_auth,font="Courier")
lbl_password_show.pack()


#(raises login frame above auth frame)
frame_login.tkraise()

root.mainloop()