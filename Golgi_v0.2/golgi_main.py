import tkinter as tk
from tkinter import ttk, PhotoImage
import customtkinter as ctk
from data_users import golgi_users
from dataframe import *
from math import ceil
from admin import *

LARGE_FONT= ("Verdana", 12)

class GolgiApp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        
        ctk.CTk.__init__(self, *args, **kwargs)

        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

        if in_linux:
            #self.iconbitmap("@Golgi_v0.2/images/logo-gradient.xbm")
            icon = PhotoImage(file = "Golgi_v0.2/images/icon-logo-gradient.png")
            self.iconphoto(True, icon)
        else:
            self.iconbitmap("@Golgi_v0.2/images/logo-gradient.ico")

        self.title('Golgi v0.2')

        self.geometry("840x400")

        container = ctk.CTkFrame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ResetPassword, AdminRegister, AdminConfig, AddUser, AdminCollect1, AdminEdit, AdminCollect2, AdminDelete):

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

