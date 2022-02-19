"""
    File:
        edit_screen.py
    Description:
        Page to etid medications from dataset
    Author:
        Pedro Croso <pedrocroso@usp.br>
"""
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
#from collect_screen import Resultado

from dataframe import *
import os

class SearchEditPage(MDBoxLayout):
    """Page to search items to edit

    Args:
        MDBoxLayout: BoxLayout from KivyMD
    """
    def __init__(self, **kwargs):
        """Initialisation function
        """
        self.nome_item = ""
        self.id_item = ""
        self.dose_item = ""
        self.apresentacao_item = ""
        self.pos_item = ""
        super().__init__(**kwargs)

    
    def edit_release(self):
        """Callback function for release of edit button
        """
        try:
            golgi_data.delete_item(int(float(self.id_item)))
        except:
            golgi_data.delete_item(self.id_item)
        finally:
            print("Error deleting item from dataset")

    def edit_press(self):
        """Callback function for pressing edit button
        """
        for item in self.ids.resultados.ids.main_layout.children:
            print("Check: ")
            print(item.ids.check_box.active)
            if item.ids.check_box.active == True:
                print("On if")
                self.nome_item = item.nome
                self.id_item = item.id
                self.dose_item = item.dose
                self.apresentacao_item = item.apresentacao
                self.pos_item = item.position
                print(item.nome)
                print("Pos: " + item.position)
                return

    def on_submit(self):
        """Callback function to search for items to edit
        """
        data = golgi_data.get_items(id = self.ids.busca.ids.id.text, nome = self.ids.busca.ids.nome.text, dosagem=self.ids.busca.ids.dose.text, apresentacao=self.ids.busca.ids.apresentacao.text)
        self.ids.resultados.ids.main_layout.clear_widgets()
        self.ids.busca.ids.nome.text = ""
        self.ids.busca.ids.id.text = ""
        self.ids.busca.ids.dose.text = ""
        self.ids.busca.ids.apresentacao.text = ""
        print(data)

        for index in data.index:
            print(index)
            new_item = ResultadoBinario()
            new_item.set_nome(str(data['nome'][index]))
            new_item.set_id(str(index))
            new_item.set_dose(str(data['dosagem'][index]))
            new_item.set_apresentacao(str(data['apresentacao'][index]))
            new_item.set_position(str(data['position'][index]))
            new_item.generate()
            self.ids.resultados.ids.main_layout.add_widget(new_item)



class EditPage(MDGridLayout):
    """Page where edition is actually made

    Args:
        MDGridLayout: GridLayout from KivyMD
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
        """Callback function to register edited item

        Returns:
            bool: True if all fields are completed
        """
        self.id = self.ids.id.text
        self.nome = self.ids.nome.text
        self.dose = self.ids.dose.text
        self.apresentacao = self.ids.apresentacao.text
        self.position = self.ids.position.text

        new_path = ""

        
        
        
        if (self.nome == "" or self.id == "" or self.dose == "" or self.apresentacao == "" or self.position == ""):
            print("Complete form!\n")
            print(self.nome + "\n")
            print(self.id + "\n")
            print(self.position + "\n")
            print(self.dose + "\n")
            print(self.apresentacao + "\n")
            return False
        else:
            #golgi_data.delete_item(int(float(self.id)))
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

class ResultadoBinario(MDBoxLayout):
    """Each individual search result layout

    Args:
        MDBoxLayout: BoxLayout from MDKivy
    """

    def __init__(self):
        """Initialisation method
        """
        self.nome = "Nome!"
        self.id = "0"
        self.dose = "Dosagem!"
        self.apresentacao = "apresentacao!"
        self.position = ""
        
        
    def generate(self, **kwargs):
        """Generates the actual widget
        """
        super().__init__(**kwargs)

    def set_nome(self, nome):
        """Set the name on search item

        Args:
            nome (str): The name

        Returns:
            [bool]: true if a string is passed as parameter
        """
        if (isinstance(nome, str)):
            self.nome = nome
            return True
        return False
    
    def set_id(self, id):
        """Set the ID on search item

        Args:
            id (str): the unique identification of item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(id, str)):
            self.id = id
            return True
        return False

    def set_dose(self, dose):
        """Set the dose on search item

        Args:
            dose (str): dose of the item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(dose, str)):
            self.dose = dose
            return True
        return False

    def set_apresentacao(self, apresentacao):
        """Set the manufacturer on search item

        Args:
            apresentacao ([str): manufactorer of the item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(apresentacao, str)):
            self.apresentacao = apresentacao
            return True
        return False

  

    def set_position(self, position):
        """Set the position of search item

        Args:
            position (str): position on robot of the item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(position, str)):
            self.position = position
            return True
        return False