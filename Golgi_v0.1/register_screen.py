"""
    File:
        register_screen.py
    Description:
       Register page for Golgibot application.
    Author:
        Pedro Croso <pedrocroso@usp.br>
"""
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
import os
import time

from dataframe import *

class RegisterPage(MDGridLayout):
    """Register Page definition

    Args:
        MDGridLayout: GridLayout from kivyMD
    """
    photo_icon = "camera"
    register_icon = "plus"

    def __init__(self, **kwargs):
        """Initialisation method
        """
        self.nome = ""
        self.id = ""
        self.dose = ""
        self.apresentacao = ""
        self.position = ""
        
        super().__init__(**kwargs)
    
    def submit_item(self):
        """Callback function to register new item in dataset

        Returns:
            bool: True if all fields were completed
        """
        self.id = self.ids.id.text
        self.nome = self.ids.nome.text
        self.dose = self.ids.dose.text
        self.apresentacao = self.ids.apresentacao.text
        self.position = self.ids.position.text
    
        

        if (self.nome == "" or self.id == "" or self.dose == "" or self.apresentacao == "" or self.position == ""):
            print("Complete form!\n")
            print(self.nome + "\n")
            print(self.id + "\n")
            print(self.position + "\n")
            print(self.dose + "\n")
            print(self.apresentacao + "\n")

            return False
        else:
            
            item =  [{
                "id": self.id,
                "nome": self.nome, 
                "dosagem": self.dose,
                "apresentacao": self.apresentacao,
                "position": self.position,
                }]
            golgi_data.add_item(item)
            golgi_data.save_to_disk()
            self.ids.nome.text = ""
            self.ids.id.text = ""
            self.ids.dose.text = ""
            self.ids.apresentacao.text = ""
            self.ids.position.text = ""

            return True
