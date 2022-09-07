"""
    File:
    
    Description:
    
    Author:
        Pedro Croso <pedrocroso@usp.br>
    """
    
import pandas as pd
from config import *


class GolgiUsers():
    """_summary_
    """
    columns = ['nusp','nome','rfid','senha','admin']
    
    def __init__(self) -> None:
        # if in_linux:
        #     self.df = pd.read_csv("Golgi_v0.2/dados/login_data.csv")
        # else:
        #     self.df = pd.read_csv("Golgi_v0.2\dados\login_data.csv")
        self.df = pd.read_csv(r"Golgi_v0.2/dados/login_data.csv")
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
        self.df = self.df.append(new_item)
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
            self.df = self.df.append(new_item)
        except:
            print("Error editing item")
    
    
    def validate(self, nusp, senha):
        df_search = self.df
        df_search =  df_search.reset_index()
        try:
            nusp = int(float(nusp))
        except:
            pass
        user = df_search[(df_search['nusp'] == nusp)]
        print("user: ")
        print(user)
        if not user.empty:
            try:
                print("on try")
                print(user.iloc[0]['senha'])
                if user.iloc[0]['senha'] == senha:
                    return True
                return False 
            except:
                print("Error validating")
                #print(user.iloc[0]['senha'])
            #finally:
            #    print("Cant't access user.iloc[0]['senha']")
    
    
    
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
        if in_linux:
            self.df.to_csv('Golgi_v0.1/dados/login_data.csv')#, index=False)
        else:
            self.df.to_csv('Golgi_v0.1\dados\login_data.csv')#, index=False)
        
golgi_users = GolgiUsers()