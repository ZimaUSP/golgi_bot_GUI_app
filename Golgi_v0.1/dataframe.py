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
    columns = ['id', 'nome', 'dosagem', 'apresentacao', 'position']
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
                "apresentacao": "TheProducer",
                "position": "ThePosition"
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
        try:
            self.df = self.df.drop(key)
        except:
            self.df = self.df.drop(int(float(key)))
        finally:
            print(f"Item number %d not found", key)



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
                "apresentacao": "TheProducer",
                "position": "ThePosition"
                }
        """
        self.df = self.df.drop(key)
        new_item = pd.DataFrame(item)
        self.df = self.df.append(new_item)


    def get_items(self, id = "0", nome = "", dosagem = "", apresentacao = ""):
        """
        Description: Search the dataframe to look for matches
        Params: 
            id = ""
            nome = ""
            dosagem = ""
            apresentacao = ""
        
        Return: A pandas dataset with match items
        """

        df_search = self.df
        df_search =  df_search.reset_index()
        print(self.df)
        try:
            id = int(float(id))
        except:
            if (id == ""):
                pass
            else:
                print("Invalid ID")
        
        if (id == ""):
            id = "NO ID"
        if (nome == ""):
            nome = "NO NOME"
        if (dosagem == ""):
            dosagem = "NO DOSE"
        if (apresentacao == ""):
            apresentacao = "NO APRES"
        

        print("Search parameters: ")
        print("Nome: ")
        print((df_search['nome'].str.contains(nome, case=False)))
        print("Dosagem: ")
        print(df_search['dosagem'].str.contains(dosagem, case=False))
        print("Apresentação: ")
        print(df_search['apresentacao'].str.contains(apresentacao, case=False))

        # Full Match
        selected_items = df_search[(df_search['nome'].str.contains(nome, case=False)) & (df_search['id'] == id) & (df_search['dosagem'].str.contains(dosagem, case=False)) & (df_search['apresentacao'].str.contains(apresentacao, case=False))]
        print("Full match")
        print(selected_items)

        # 3/4 Match
        selected_items = selected_items.append(df_search[(df_search['id'] == id) &   (df_search['nome'].str.contains(nome, case=False))  & (~(df_search['dosagem'].str.contains(dosagem, case=False))) &   (df_search['apresentacao'].str.contains(apresentacao, case=False)) ])
        selected_items = selected_items.append(df_search[(df_search['id'] == id) &   (df_search['nome'].str.contains(nome, case=False))  &   (df_search['dosagem'].str.contains(dosagem, case=False))  & (~(df_search['apresentacao'].str.contains(apresentacao, case=False)))])
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (~(df_search['nome'].str.contains(nome, case=False))) &   (df_search['dosagem'].str.contains(dosagem, case=False))  &   (df_search['apresentacao'].str.contains(apresentacao, case=False)) ])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) &   (df_search['nome'].str.contains(nome, case=False))  &   (df_search['dosagem'].str.contains(dosagem, case=False))  &   (df_search['apresentacao'].str.contains(apresentacao, case=False)) ])
        print("3/4 match")
        print(selected_items)

        # 2/4 match
        selected_items = selected_items.append(df_search[(df_search['id'] == id) &   (df_search['nome'].str.contains(nome, case=False))  & (~(df_search['dosagem'].str.contains(dosagem, case=False))) & (~(df_search['apresentacao'].str.contains(apresentacao, case=False)))])
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (~(df_search['nome'].str.contains(nome, case=False))) & (~(df_search['dosagem'].str.contains(dosagem, case=False))) &   (df_search['apresentacao'].str.contains(apresentacao, case=False)) ])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) &   (df_search['nome'].str.contains(nome, case=False))  & (~(df_search['dosagem'].str.contains(dosagem, case=False))) &   (df_search['apresentacao'].str.contains(apresentacao, case=False)) ])
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (~(df_search['nome'].str.contains(nome, case=False))) &   (df_search['dosagem'].str.contains(dosagem, case=False))  & (~(df_search['apresentacao'].str.contains(apresentacao, case=False)))])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) &   (df_search['nome'].str.contains(nome, case=False))  &   (df_search['dosagem'].str.contains(dosagem, case=False))  & (~(df_search['apresentacao'].str.contains(apresentacao, case=False)))])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (~(df_search['nome'].str.contains(nome, case=False))) &   (df_search['dosagem'].str.contains(dosagem, case=False))  &   (df_search['apresentacao'].str.contains(apresentacao, case=False)) ])
        print("2/4 match")
        print(selected_items)

        # 1/4 match
        selected_items = selected_items.append(df_search[(df_search['id'] == id) & (~(df_search['nome'].str.contains(nome, case=False))) & (~(df_search['dosagem'].str.contains(dosagem, case=False))) & (~(df_search['apresentacao'].str.contains(apresentacao, case=False)))])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) &   (df_search['nome'].str.contains(nome, case=False))  & (~(df_search['dosagem'].str.contains(dosagem, case=False))) & (~(df_search['apresentacao'].str.contains(apresentacao, case=False)))])
        print((df_search['nome'].str.contains(nome)))
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (~(df_search['nome'].str.contains(nome, case=False))) & (~(df_search['dosagem'].str.contains(dosagem, case=False))) &   (df_search['apresentacao'].str.contains(apresentacao, case=False)) ])
        selected_items = selected_items.append(df_search[(df_search['id'] != id) & (~(df_search['nome'].str.contains(nome, case=False))) &   (df_search['dosagem'].str.contains(dosagem, case=False))  & (~(df_search['apresentacao'].str.contains(apresentacao, case=False)))])
        print("1/4 match")
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
        "apresentacao": ["TheProducer"],
        "position": ["ThePosition"]
        }

df = pd.DataFrame(item)
df.set_index('id')
df.to_csv('Golgi_v0.1\dados\drug_data.csv', index=False)'''
