"""
    File:
        dataframe.py
    Description:
        Declaration of dataset used in GolgiBot
    Author:
        Pedro Croso <pedrocroso@usp.br>
"""

import pandas as pd


class GolgiDataFrame():
    """Class for the DataSet
    """
    columns = ['id', 'nome', 'dosagem', 'fabricante', 'position', 'photo_path']
    def __init__(self) -> None:
        self.df = pd.read_csv("Golgi_v0.1\dados\drug_data.csv")
        self.df = self.df.set_index('id')

    def add_item(self, item):
        """
        Description:
            Add a new item to drugs data frame
        Params: 
            item: list of dictionaries
             {
                "id": "TheID",
                "nome": "TheName", 
                "dosagem": "TheDose",
                "fabricante": "TheProducer",
                "position": "ThePosition",
                "photo_path": "ThePath"
                }

        """
        new_item = pd.DataFrame(item)
        new_item = new_item.set_index('id')
        self.df = self.df.append(new_item)

    def delete_item(self, key):
        """
        Description: delete item with desired key
        Params:
            key(int): id of item to be removed
        """
        self.df = self.df.drop(key)



    def modify_item(self, key, item):
        """
        Description: Modify an drug item from the dataset
        Params:
            key(int): key for the item id
            item(dictionary): 
                {
                "id": "TheID",
                "nome": "TheName", 
                "dosagem": "TheDose",
                "fabricante": "TheProducer",
                "position": "ThePosition",
                "photo_path": "ThePath"
                }
        """
        self.df = self.df.drop(key)
        new_item = pd.DataFrame(item)
        self.df = self.df.append(new_item)


    def get_items(self, id = "0", nome = "", dosagem = "", fabricante = ""):
        """
        Description: Search the dataframe to look for matches
        Params: 
            id = ""
            nome = ""
            dosagem = ""
            fabricante = ""
        
        Return: A pandas dataset with match items
        """

        df_search = self.df
        df_search =  df_search.reset_index()
        print(self.df)
        id = int(float(id))
        
        # Full Match
        selected_items = df_search[(df_search['nome'] == nome) & (df_search['id'] == id) & (df_search['dosagem']) & (df_search['fabricante'] == fabricante) & (df_search['dosagem'] == dosagem)]

        # 3/4 Match
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (df_search['nome'] == nome) & (df_search['dosagem']) & (df_search['fabricante'] == fabricante) & (df_search['dosagem'] != dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (df_search['nome'] == nome) & (df_search['dosagem']) & (df_search['fabricante'] != fabricante) & (df_search['dosagem'] == dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (df_search['nome'] != nome) & (df_search['dosagem']) & (df_search['fabricante'] == fabricante) & (df_search['dosagem'] == dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (df_search['nome'] == nome) & (df_search['dosagem']) & (df_search['fabricante'] == fabricante) & (df_search['dosagem'] == dosagem)])

        # 2/4 match
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (df_search['nome'] == nome) & (df_search['dosagem']) & (df_search['fabricante'] != fabricante) & (df_search['dosagem'] != dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (df_search['nome'] != nome) & (df_search['dosagem']) & (df_search['fabricante'] == fabricante) & (df_search['dosagem'] != dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (df_search['nome'] == nome) & (df_search['dosagem']) & (df_search['fabricante'] == fabricante) & (df_search['dosagem'] != dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (df_search['nome'] != nome) & (df_search['dosagem']) & (df_search['fabricante'] != fabricante) & (df_search['dosagem'] == dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (df_search['nome'] == nome) & (df_search['dosagem']) & (df_search['fabricante'] != fabricante) & (df_search['dosagem'] == dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (df_search['nome'] != nome) & (df_search['dosagem']) & (df_search['fabricante'] == fabricante) & (df_search['dosagem'] == dosagem)])

        # 1/4 match
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (df_search['nome'] != nome) & (df_search['dosagem']) & (df_search['fabricante'] != fabricante) & (df_search['dosagem'] != dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (df_search['nome'] == nome) & (df_search['dosagem']) & (df_search['fabricante'] != fabricante) & (df_search['dosagem'] != dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (df_search['nome'] != nome) & (df_search['dosagem']) & (df_search['fabricante'] == fabricante) & (df_search['dosagem'] != dosagem)])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (df_search['nome'] != nome) & (df_search['dosagem']) & (df_search['fabricante'] != fabricante) & (df_search['dosagem'] == dosagem)])
        
        print (selected_items)
        selected_items = selected_items.set_index('id')

        return selected_items

    def save_to_disk(self):
        """
        Description: saves the dataset to a .csv file
        """
        self.df.to_csv('Golgi_v0.1\dados\drug_data.csv')#, index=False)


golgi_data = GolgiDataFrame()

'''item = {
        "id": ["00000"],
        "nome": ["TheName"], 
        "dosagem": ["TheDose"],
        "fabricante": ["TheProducer"],
        "position": ["ThePosition"],
        "photo_path": ["ThePath"]
        }

df = pd.DataFrame(item)
df.set_index('id')
df.to_csv('Golgi_v0.1\dados\drug_data.csv', index=False)'''
