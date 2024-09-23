import tkinter as tk
from tkinter import ttk, PhotoImage
import customtkinter as ctk
from data_users import golgi_users
from dataframe import *
from math import ceil
from pages import *

LARGE_FONT= ("Verdana", 12)

class GolgiApp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        
        ctk.CTk.__init__(self, *args, **kwargs)

        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

        icon = PhotoImage(file = "images/icon-logo-gradient.png")
        self.iconphoto(True, icon)

        self.title('Golgi v0.2')

        self.geometry("940x420")
        self.minsize(940, 420)

        container = ctk.CTkFrame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ResetPassword, Register, Config, AddUser, CollectInfo, Edit, Collect, Delete):

            frame = CTkFrame(container, fg_color="transparent")

            page = F(frame, self)
            page.pack(fill="both", expand=True)
            if (F not in {StartPage, ResetPassword} ):
                menu = Menu(frame, F, self)
                menu.pack()

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

if __name__ == '__main__':
    app = GolgiApp()
    app.mainloop()

