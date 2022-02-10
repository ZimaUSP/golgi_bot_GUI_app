"""
    File:
        delete_screen.py
    Description:
        Page to delete medications from dataset
    Author:
        Pedro Croso <pedrocroso@usp.br>
"""
from kivymd.uix.boxlayout import MDBoxLayout
from edit_screen import ResultadoBinario

from dataframe import *

import os

class DeletePage(MDBoxLayout):
    """Page to delete item

    Args:
        MDBoxLayout: BoxLayout from MDKivy
    """
    def __init__(self, **kwargs):
        """Initialisation method
        """
        super().__init__(**kwargs)
    
    def on_submit(self):
        """Callback function to search for results
        """
        data = golgi_data.get_items(id = self.ids.busca.ids.id.text, nome = self.ids.busca.ids.nome.text, dosagem=self.ids.busca.ids.dose.text, apresentacao=self.ids.busca.ids.apresentacao.text)
        self.ids.resultados.ids.main_layout.clear_widgets()
        self.ids.busca.ids.nome.text = ""
        self.ids.busca.ids.id.text = ""
        self.ids.busca.ids.dose.text = ""
        self.ids.busca.ids.apresentacao.text = ""
        data = data.reset_index()
        for index in data.index:
            new_item = ResultadoBinario()
            new_item.set_nome(str(data['nome'][index]))
            new_item.set_id(str(data['id'][index]))
            new_item.set_dose(str(data['dosagem'][index]))
            new_item.set_apresentacao(str(data['apresentacao'][index]))
            new_item.set_photo_path(str(data['photo_path'][index]))
            new_item.set_position(str(data['position'][index]))
            new_item.generate()
            self.ids.resultados.ids.main_layout.add_widget(new_item)
        
    def delete_release(self):
        """Callback function to delete the selected items
        """
        for item in self.ids.resultados.ids.main_layout.children:
            print("Check: ")
            print(item.ids.check_box.active)
            if item.ids.check_box.active == True:
                print("On if")
                os.remove(item.photo_path)
                golgi_data.delete_item(item.id)#int(float(item.id)))
                golgi_data.save_to_disk()
                self.ids.resultados.ids.main_layout.remove_widget(item)
