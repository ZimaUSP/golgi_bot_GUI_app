"""
    File:
        golgi_main.py
    Description:
        Main script for Golgibot application.
    Author:
        Pedro Croso <pedrocroso@usp.br>
"""
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager


from main_screen import *
from collect_screen import *
from log_in_screen import *
from register_screen import *
from delete_screen import *
from edit_screen import *

from dataframe import *




Builder.load_file('main_screen.kv')
Builder.load_file('collect_screen.kv')
Builder.load_file('log_in_screen.kv')
Builder.load_file('register_screen.kv')
Builder.load_file('delete_screen.kv')
Builder.load_file('edit_screen.kv')

Builder.load_file('main.kv')

#Screen Definitions

class LogInScreen(MDScreen):
    """Declaration of Log In screen

    Args:
        MDScreen
    """
    pass

class EditScreen(MDScreen):
    """Declaration of edit screen

    Args:
        MDScreen
    """
    def __init__(self, **kw):
        """Initialisation method
        """
        super().__init__(**kw)
    
    def on_pre_enter(self, *args):
        """Callback funtion called before entering the screen. Sets text fields and variables
        """

        nome = self.manager.get_screen("main_screen").ids.main_page.ids.search_edit_page.nome_item
        id = self.manager.get_screen("main_screen").ids.main_page.ids.search_edit_page.id_item
        dose = self.manager.get_screen("main_screen").ids.main_page.ids.search_edit_page.dose_item
        apresentacao = self.manager.get_screen("main_screen").ids.main_page.ids.search_edit_page.apresentacao_item
        position = self.manager.get_screen("main_screen").ids.main_page.ids.search_edit_page.pos_item
        photo_path = ""
        if app.current_screen == "camera_screen":
            print("Returning from camera")
            os.remove(self.manager.get_screen("main_screen").ids.main_page.ids.search_edit_page.photo_path_item)
            photo_path = self.manager.get_screen("camera_screen").ids.camera_page.last_img_name
        else:
            photo_path = self.manager.get_screen("main_screen").ids.main_page.ids.search_edit_page.photo_path_item



        self.ids.edit_page.nome = nome
        self.ids.edit_page.id = id
        self.ids.edit_page.dose = dose
        self.ids.edit_page.apresentacao = apresentacao
        self.ids.edit_page.position = position
        self.ids.edit_page.photo_path = photo_path

        self.ids.edit_page.ids.nome.text = nome
        self.ids.edit_page.ids.id.text = id
        self.ids.edit_page.ids.dose.text = dose
        self.ids.edit_page.ids.apresentacao.text = apresentacao
        self.ids.edit_page.ids.position.text = position
        self.ids.edit_page.ids.imagem_remedio.source = photo_path


        print("Nome na main: " + self.manager.get_screen("main_screen").ids.main_page.ids.search_edit_page.nome_item)
        print("Nome: " + self.ids.edit_page.nome)


        return super().on_pre_enter(*args)

class MainScreen(MDScreen):
    """Declaration of main screen

    Args:
        MDScreen: Screen from KivyMD
    """
    def __init__(self, **kw):
        """Initialisation method
        """
        super().__init__(**kw)
    
    def on_enter(self, *args):
        """Callback function for entering the screen. Configures some Text Inputs and images.
        """

        
        self.ids.main_page.ids.register_page.photo_path = self.manager.get_screen("camera_screen").ids.camera_page.last_img_name

        print(self.manager.get_screen("camera_screen").ids.camera_page.last_img_name)
        print(self.ids.main_page.ids.register_page.photo_path)
        self.ids.main_page.ids.register_page.ids.imagem_remedio.source = self.manager.get_screen("camera_screen").ids.camera_page.last_img_name
        self.ids.main_page.ids.register_page.ids.imagem_remedio.reload()
        return super().on_enter(*args)

class CameraScreen(MDScreen):
    """Declaration of Camera Screen

    Args:
        MDScreen: Screen from KivyMD
    """
    def __init__(self, **kw):
        """Initialisation method
        """
        super().__init__(**kw)
    
    def on_enter(self, *args):
        """Callback function to enter Camera Screen. Enables camera.
        """
        self.ids.camera_page.ids.camera.play = True
        return super().on_enter(*args)
    
    def on_leave(self, *args):
        """Callback function to exit Camera Screen. Disables Camera
        """
        self.ids.camera_page.ids.camera.play = False

        return super().on_leave(*args)


class WindowManager(ScreenManager):
    """Window Manager Declaration"""
    pass


class GolgiApp(MDApp):
    """Main App declaration

    Args:
        MDApp: App from KivyMD
    """
    def __init__(self, **kwargs):
        """Initialisation method
        """
        super().__init__(**kwargs)
        self.previous_screen = ""
        self.current_screen = ""


    def build(self):
        """Build method

        """
        self.icon = 'images\logo-gradient.png'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        return WindowManager()



app = GolgiApp()
app.run()