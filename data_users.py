"""
    File:
    
    Description:
    
    Author:
        Pedro Croso <pedrocroso@usp.br>
    """
    
import pandas as pd
from config import *
from tkinter import *
from tkinter import messagebox

class GolgiUsers():
    """_summary_
    """
    columns = ['nusp','nome','rfid','senha','admin']
    
    def __init__(self) -> None:
        self.df = pd.read_csv("dados/login_data.csv")
        self.df = self.df.set_index('nusp')
    
    def add_user(self, item):
        """
        Description:
            Add a new user to login data frame
        Params: 
            item: list of dictionaries
             {
                "nusp": "TheNUSP",
                "nome": "TheName", 
                "rfid": "TheRFID",
                "senha": "ThePassword",
                "admin": "TheAdmin"
                }

        """
        new_item = pd.DataFrame(item)
        print(new_item)
        new_item = new_item.set_index('nusp')
        self.df = pd.concat([self.df, new_item])
        print(self.df)
    
    def remove_user(self, nusp):
        """
        Description: delete user with desired nusp
        Params:
            key(int): nusp of user to be removed
        """
        try:
            self.df = self.df.drop(nusp)
        except:
            self.df = self.df.drop(int(float(nusp)))
        finally:
            print(f"Item number %d not found", nusp)
        
    
    def modify_item(self, nusp, item):
        """
        Description: Modify an drug item from the dataset
        Params:
            key(int): key for the item id
            item(dictionary): 
                 {
                "nusp": "TheNUSP",
                "nome": "TheName", 
                "rfid": "TheRFID",
                "senha": "ThePassword",
                "admin": "TheAdmin"
                }
        """
        try:
            self.remove_user(nusp)
            new_item = pd.DataFrame(item)
            self.df = pd.concat([self.df, new_item])
        except:
            print("Error editing item")
    
    
    def validate(self, nusp, senha):
        df_search = self.df
        df_search =  df_search.reset_index()
        try:
            nusp = int(float(nusp))
        except ValueError:
            print("O usuario deveria ser um numero inteiro")
            messagebox.showinfo(title="Erro", message="O usuário deveria ser um número inteiro")
            return False
        user = df_search[(df_search['nusp'] == nusp)]
        print("user: ")
        print(user)
        if not user.empty:
            try:
                print("on try")
                print(user.iloc[0]['senha'])
                if user.iloc[0]['senha'] == senha:
                    return True
                messagebox.showinfo(title="Erro", message="Senha Inválida")
                print("Senha Invalida")
                return False 
            except:
                print("Error validating")
                #print(user.iloc[0]['senha'])
            #finally:
            #    print("Cant't access user.iloc[0]['senha']")
        else:
            print("Usuario nao encontrado")
            messagebox.showinfo(title="Erro", message="Usuário não encontrado")
    
    def get_admin(self, nusp):
        print("getting admin")
        df_search = self.df
        df_search =  df_search.reset_index()
        try:
            nusp = int(float(nusp))
        except:
            pass
        user = df_search[(df_search['nusp'] == nusp)]
        print(user)
        if not user.empty:
            print(user.iloc[0]['admin'])
            if user.iloc[0]['admin'] == True:
                return True
            return False
        
    
    def save_to_disk(self):
        """
        Description: saves the dataset to a .csv file
        """
        self.df.to_csv('dados/login_data.csv')#, index=False)
       
golgi_users = GolgiUsers()
