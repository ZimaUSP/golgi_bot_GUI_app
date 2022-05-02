"""
    File:
        add_user_screen.py
    Description:
       Add user page for Golgibot application.
    Author:
        Pedro Croso <pedrocroso@usp.br>
"""
from kivymd.uix.gridlayout import MDGridLayout
from data_users import *

from dataframe import *

class AddUserPage(MDGridLayout):
    """Register Page definition

    Args:
        MDGridLayout: GridLayout from kivyMD
    """
    register_icon = "plus"

    def __init__(self, **kwargs):
        """Initialisation method
        """
        self.nome = ""
        self.nusp = ""
        self.rfid = ""
        self.senha = ""
        self.senha_verify = ""
        self.is_new_user_admin = False
        
        super().__init__(**kwargs)
    
    def submit_user(self):
        """Callback function to register new user in dataset

        Returns:
            bool: True if all fields were completed
        """
        self.nome = self.ids.nome.text
        self.nusp = self.ids.nusp.text
        self.rfid = self.ids.rfid.text
        self.senha = self.ids.senha.text
        self.senha_verify = self.ids.senha_verify.text
        self.is_new_user_admin = self.ids.is_new_user_admin.active
    
        

        if (self.nome == "" or self.nusp == "" or self.rfid == "" or self.senha == "" or self.senha_verify == ""):
            print("Complete form!\n")
            print(self.nome + "\n")
            print(self.nusp + "\n")
            print(self.rfid + "\n")
            print(self.senha + "\n")
            print(self.senha_verify + "\n")

            return False
        elif self.senha != self.senha_verify:
            print ("Senha não corresponde! ")
        else:
            
            user =  [{
                "nusp": self.nusp,
                "nome": self.nome, 
                "rfid": self.rfid,
                "senha": self.senha,
                "admin": self.is_new_user_admin,
                }]
            
            golgi_users.add_user(user)
            golgi_users.save_to_disk()
            
            '''golgi_data.add_item(item)
            golgi_data.save_to_disk()
            self.ids.nome.text = ""
            self.ids.nusp.text = ""
            self.ids.dose.text = ""
            self.ids.apresentacao.text = ""
            self.ids.position.text = ""'''

            return True
