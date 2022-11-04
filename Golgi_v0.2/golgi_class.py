import tkinter as tk
from tkinter import ttk
from data_users import golgi_users
from dataframe import *
from math import ceil
from admin import *


LARGE_FONT= ("Verdana", 12)

# Define button functions
def reset_password(controller):
    controller.show_frame(ResetPassword)
    return

def login(user, password, controller):
    #add popup if wrong password
    checker = golgi_users.validate(user, password)
    adm = golgi_users.get_admin(user)

    if checker:
        controller.show_frame(AdminCollect1)
        # if adm:
        #     controller.show_frame(Register)
        # else:
        #     controller.show_frame(Register)

    return


class GolgiApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.iconbitmap("Golgi_v0.2/images/logo-gradient.ico")

        self.title('Golgi v0.2')

        self.geometry("600x600")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ResetPassword, AdminRegister, Help, AddUser, AdminCollect1, AdminEdit, AdminCollect2, AdminDelete):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

if __name__ == '__main__':
    app = GolgiApp()
    app.mainloop()