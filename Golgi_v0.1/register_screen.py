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
        self.photo_path = "foto_remedio\paracetamol_500mg.jpg"
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
    
        new_path = self.photo_path[23:]
        new_path = "Golgi_v0.1\dados\images" + new_path
        #self.photo_path = new_path

        if (self.nome == "" or self.id == "" or self.dose == "" or self.apresentacao == "" or self.position == ""):
            print("Complete form!\n")
            print(self.photo_path + "\n")
            print(self.nome + "\n")
            print(self.id + "\n")
            print(self.position + "\n")
            print(self.dose + "\n")
            print(self.apresentacao + "\n")

            return False
        else:
            #new_path = self.photo_path[23:]
            #new_path = "Golgi_v0.1\dados\images" + new_path
            os.rename(self.photo_path, new_path)
            self.photo_path = new_path
            item =  [{
                "id": self.id,
                "nome": self.nome, 
                "dosagem": self.dose,
                "apresentacao": self.apresentacao,
                "position": self.position,
                "photo_path": self.photo_path
                }]
            golgi_data.add_item(item)
            golgi_data.save_to_disk()
            self.ids.nome.text = ""
            self.ids.id.text = ""
            self.ids.dose.text = ""
            self.ids.apresentacao.text = ""
            self.ids.position.text = ""
            self.photo_path = "foto_remedio\paracetamol_500mg.jpg"
            self.ids.imagem_remedio.source = self.photo_path

            return True
    



class CameraPage(MDBoxLayout):
    """Camera page definition

    Args:
        MDBoxLayout: BoxLayout from KivyMD
    """
    def __init__(self, **kwargs):
        """Initialisation method
        """
        self.last_img_name = "foto_remedio\paracetamol_500mg.jpg"
        super().__init__(**kwargs)

    def take_photo(self):
        """Callback function to take a picture from camera
        """
        print(self.ids.camera.play)
        if(self.ids.camera.play):
            try:
                if (self.last_img_name != "foto_remedio\paracetamol_500mg.jpg"):
                    os.remove(self.last_img_name)
            except Exception:
                print(Exception)
                print("file not found!")
            timestr = time.strftime("%Y%m%d_%H%M%S")
            self.ids.camera.export_to_png("Golgi_v0.1\\foto_remedio\IMG_{}.png".format(timestr))
            self.last_img_name = "Golgi_v0.1\\foto_remedio\IMG_{}.png".format(timestr)
            print("Captured")
    
