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
        
        file_path = "dados/current_port.txt"
        with open(file_path, "r") as file:
            self.esp_port = file.read()


        ctk.CTk.__init__(self, *args, **kwargs)
        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

        icon = PhotoImage(file = "images/icon-logo-gradient.png")
        self.iconphoto(True, icon)

        self.attributes('-fullscreen', True)
        self.title('Golgi v0.2')

        self.geometry("940x420")
        self.minsize(940, 420)

        self.container = ctk.CTkFrame(self)

        self.container.pack(side="top", fill="both", expand = True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ResetPassword, Register, Config, Ports, AddUser, CollectInfo, Edit, Collect, Delete):

            frame = CTkFrame(self.container, fg_color="transparent")

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
    
    def create_page(self, cont):
        if cont in self.frames.keys():
            if self.frames[cont] is None:

                frame = CTkFrame(self.container, fg_color="transparent")

                page = cont(frame, self)
                page.pack(fill="both", expand=True)
            
                if (cont not in {StartPage, ResetPassword} ):
                    menu = Menu(frame, cont, self)
                    menu.pack()
            
                self.frames[cont] = frame

                frame.grid(row=0, column=0, sticky="nsew")
        else:

            frame = CTkFrame(self.container, fg_color="transparent")

            page = cont(frame, self)
            page.pack(fill="both", expand=True)
            
            if (cont not in {StartPage, ResetPassword} ):
                menu = Menu(frame, cont, self)
                menu.pack()
            
            self.frames[cont] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

    def destroy_page(self, cont):
        for page in self.frames.keys():
            if page == cont:
                self.frames[cont] = None
                break
    
    def update_page(self, cont):
        self.destroy_page(cont)
        self.create_page(cont)



if __name__ == '__main__':
    app = GolgiApp()
    app.mainloop()

