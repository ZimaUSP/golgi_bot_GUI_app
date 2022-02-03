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
from collect_screen import Resultado

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
        self.fabricante_item = ""
        self.photo_path_item = ""
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
                self.fabricante_item = item.fabricante
                self.photo_path_item = item.photo_path
                self.pos_item = item.position
                print(item.nome)
                print("Pos: " + item.position)
                return

    def on_submit(self):
        """Callback function to search for items to edit
        """
        data = golgi_data.get_items(id = self.ids.busca.ids.id.text, nome = self.ids.busca.ids.nome.text, dosagem=self.ids.busca.ids.dose.text, fabricante=self.ids.busca.ids.fabricante.text)
        self.ids.resultados.ids.main_layout.clear_widgets()
        self.ids.busca.ids.nome.text = ""
        self.ids.busca.ids.id.text = ""
        self.ids.busca.ids.dose.text = ""
        self.ids.busca.ids.fabricante.text = ""
        print(data)

        for index in data.index:
            print(index)
            new_item = Resultado()
            new_item.set_nome(str(data['nome'][index]))
            new_item.set_id(str(index))
            new_item.set_dose(str(data['dosagem'][index]))
            new_item.set_fabricante(str(data['fabricante'][index]))
            new_item.set_photo_path(str(data['photo_path'][index]))
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
        self.photo_path = "foto_remedio\paracetamol_500mg.jpg"
        self.nome = ""
        self.id = ""
        self.dose = ""
        self.fabricante = ""
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
        self.fabricante = self.ids.fabricante.text
        self.position = self.ids.position.text

        new_path = ""

        if self.photo_path[:23] != "Golgi_v0.1\dados\images":
            print("Current path: " + self.photo_path)
            new_path = self.photo_path[23:]
            new_path = "Golgi_v0.1\dados\images" + new_path
            print("New path: " + new_path)

        
        
        
        if (self.nome == "" or self.id == "" or self.dose == "" or self.fabricante == "" or self.position == ""):
            print("Complete form!\n")
            print(self.photo_path + "\n")
            print(self.nome + "\n")
            print(self.id + "\n")
            print(self.position + "\n")
            print(self.dose + "\n")
            print(self.fabricante + "\n")
            return False
        else:
            #golgi_data.delete_item(int(float(self.id)))
            if new_path != "":
                os.rename(self.photo_path, new_path)
                self.photo_path = new_path
            item =  [{
                "id": self.id,
                "nome": self.nome, 
                "dosagem": self.dose,
                "fabricante": self.fabricante,
                "position": self.position,
                "photo_path": self.photo_path
                }]
            golgi_data.add_item(item)
            golgi_data.save_to_disk()
            self.ids.nome.text = ""
            self.ids.id.text = ""
            self.ids.dose.text = ""
            self.ids.fabricante.text = ""
            self.ids.position.text = ""
            self.photo_path = "foto_remedio\paracetamol_500mg.jpg"
            self.ids.imagem_remedio.source = self.photo_path

            return True