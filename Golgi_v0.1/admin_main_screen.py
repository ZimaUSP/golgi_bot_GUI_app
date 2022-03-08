from main_screen import *
from kivymd.uix.boxlayout import MDBoxLayout

class AdminMainPage(MDBoxLayout):
    """Main Admin Screen declaration

    Args:
        MDBoxLayout: BoxLayout from KivyMD
    """
    def __init__(self, **kwargs):
        """Initialisation method
        """
        super().__init__(**kwargs)