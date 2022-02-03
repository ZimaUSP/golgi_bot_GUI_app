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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def collect_release(self):
        print (self.ids.resultados.ids)
    
    def on_submit(self):
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
        '''for i in range(2):
            new_item = Resultado()
            new_item.set_nome("Nome " + str(i))
            new_item.set_id("ID " + str(i))
            new_item.set_dose("Dose " + str(i))
            new_item.set_fabricante("Fabricante " + str(i))
            new_item.generate()
            self.ids.resultados.ids.main_layout.add_widget(new_item)'''
        

class Busca(MDBoxLayout):
    pass

class Resultados(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #print(self.ids)
        #for i in range(20):
        #    self.ids.main_layout.add_widget(Button())

class Resultado(MDBoxLayout):

    def __init__(self):
        self.nome = "Nome!"
        self.id = "0"
        self.dose = "Dosagem!"
        self.fabricante = "Fabricante!"
        self.photo_path = "images\paracetamol_500mg.jpg"
        self.position = ""
        
        
    def generate(self, **kwargs):
        super().__init__(**kwargs)

    def set_nome(self, nome):
        if (isinstance(nome, str)):
            self.nome = nome
            return True
        return False
    
    def set_id(self, id):
        if (isinstance(id, str)):
            self.id = id
            return True
        return False

    def set_dose(self, dose):
        if (isinstance(dose, str)):
            self.dose = dose
            return True
        return False

    def set_fabricante(self, fabricante):
        if (isinstance(fabricante, str)):
            self.fabricante = fabricante
            return True
        return False

    def set_photo_path(self, photo_path):
        if (os.path.exists(photo_path)):
            self.photo_path = photo_path
            return True
        return False

    def set_position(self, position):
        if (isinstance(position, str)):
            self.position = position
            return True
        return False

        
