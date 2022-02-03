"""
    File:
        collect_screen.py
    Description:
        Page to search for medications and request machinne to grab one or multiple
    Author:
        Pedro Croso <pedrocroso@usp.br>
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView

import os

from dataframe import *

class CollectPage(MDBoxLayout):
    """Page Layout for the CollectScreen

    Args:
        MDBoxLayout (): BoxLayout from MDKivy
    """
    def __init__(self, **kwargs):
        """Initialise CollectPage
        """
        super().__init__(**kwargs)
    
    def collect_release(self):

        print (self.ids.resultados.ids)
    
    def on_submit(self):
        """Callback function so search itens from Pandas dataset
        """
        data = golgi_data.get_items(id = self.ids.busca.ids.id.text, nome = self.ids.busca.ids.nome.text, dosagem=self.ids.busca.ids.dose.text, fabricante=self.ids.busca.ids.fabricante.text)
        self.ids.resultados.ids.main_layout.clear_widgets()
        self.ids.busca.ids.nome.text = ""
        self.ids.busca.ids.id.text = ""
        self.ids.busca.ids.dose.text = ""
        self.ids.busca.ids.fabricante.text = ""
        data = data.reset_index()
        for index in data.index:
            new_item = Resultado()
            new_item.set_nome(str(data['nome'][index]))
            new_item.set_id(str(data['id'][index]))
            new_item.set_dose(str(data['dosagem'][index]))
            new_item.set_fabricante(str(data['fabricante'][index]))
            new_item.set_photo_path(str(data['photo_path'][index]))
            new_item.set_position(str(data['position'][index]))
            new_item.generate()
            self.ids.resultados.ids.main_layout.add_widget(new_item)
        
        

class Busca(MDBoxLayout):
    """Definition for the search layout used in CollectPage

    Args:
        MDBoxLayout: BoxLayout from MDKivy
    """
    pass

class Resultados(ScrollView):
    """Layout where results show up

    Args:
        ScrollView ([type]): [description]
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #print(self.ids)
        #for i in range(20):
        #    self.ids.main_layout.add_widget(Button())

class Resultado(MDBoxLayout):
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
        self.fabricante = "Fabricante!"
        self.photo_path = "images\paracetamol_500mg.jpg"
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

    def set_fabricante(self, fabricante):
        """Set the manufacturer on search item

        Args:
            fabricante ([str): manufactorer of the item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(fabricante, str)):
            self.fabricante = fabricante
            return True
        return False

    def set_photo_path(self, photo_path):
        """Set the photo path on search item

        Args:
            photo_path (str): relative path to photo on item
        Returns:
            [bool]: true if a string is passed
        """
        if (os.path.exists(photo_path)):
            self.photo_path = photo_path
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

        
