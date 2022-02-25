"""
    File:
        delete_screen.py
    Description:
        Page to delete medications from dataset
    Author:
        Pedro Croso <pedrocroso@usp.br>
"""
from math import ceil
from kivymd.uix.boxlayout import MDBoxLayout
from edit_screen import ResultadoBinario

from dataframe import *
from visual_components.busca import *
from visual_components.resultado_busca import *



class DeletePage(MDBoxLayout):
    """Page to delete item

    Args:
        MDBoxLayout: BoxLayout from MDKivy
    """
    def __init__(self, **kwargs):
        """Initialisation method
        """
        self.current_page = 0
        super().__init__(**kwargs)
    
    def on_submit(self):
        """Callback function to search for results
        """
        self.data = golgi_data.get_items(id = self.ids.busca.ids.id.text, nome = self.ids.busca.ids.nome.text, dosagem=self.ids.busca.ids.dose.text, apresentacao=self.ids.busca.ids.apresentacao.text)
        #self.ids.resultados.ids.main_layout_resultados.clear_widgets()
        self.ids.busca.ids.nome.text = ""
        self.ids.busca.ids.id.text = ""
        self.ids.busca.ids.dose.text = ""
        self.ids.busca.ids.apresentacao.text = ""
        self.data = self.data.reset_index()
        self.n_items  = len(self.data.index)
        self.n_pages = ceil(self.n_items/15.0)
        self.current_page = 0
        self.ids.current_page.text = "1"
        self.ids.go_to_last.text = str(self.n_pages)
        self.load_items()
        
        print(self.n_items)
    
    def load_items(self):
        self.ids.main_layout_resultados.clear_widgets()
        self.ids.current_page.text = str(self.current_page + 1)
        for index in range(15): #self.data.index:
            index = 15*self.current_page + index
            if index < self.n_items:
                new_item = ResultadoBinario()
                new_item.set_nome(str(self.data['nome'][index]))
                new_item.set_id(str(self.data['id'][index]))
                new_item.set_dose(str(self.data['dosagem'][index]))
                new_item.set_apresentacao(str(self.data['apresentacao'][index]))
                new_item.set_position(str(self.data['position'][index]))
                new_item.generate()
                #self.ids.resultados.ids.main_layout_resultados.add_widget(new_item)
                self.ids.main_layout_resultados.add_widget(new_item)
    
    def on_go_to_first(self):
        self.current_page = 0
        self.load_items()
    
    def on_go_to_previous(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.load_items()
    
    def on_go_to_next(self):
        if self.current_page < self.n_pages - 1:
            self.current_page += 1
            self.load_items()
    
    def on_go_to_last(self):
        self.current_page = self.n_pages - 1
        self.load_items()
    

        
    def delete_release(self):
        """Callback function to delete the selected items
        """
        for item in self.ids.main_layout_resultados.children:
            print("Check: ")
            print(item.ids.check_box.active)
            if item.ids.check_box.active == True:
                print("On if")
                golgi_data.delete_item(item.id)#int(float(item.id)))
                golgi_data.save_to_disk()
                self.ids.main_layout_resultados.remove_widget(item)
