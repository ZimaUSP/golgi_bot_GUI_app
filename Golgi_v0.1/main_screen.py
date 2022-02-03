from kivymd.uix.boxlayout import MDBoxLayout


class MainPage(MDBoxLayout):
    """Main Screen declaration

    Args:
        MDBoxLayout: BoxLayout from KivyMD
    """
    def __init__(self, **kwargs):
        """Initialisation method
        """
        super().__init__(**kwargs)
    
    def on_collect_enter(self):
        """Callback function to entering collect section
        """
        self.ids.collect_page.ids.busca.ids.nome.text = ""
        self.ids.collect_page.ids.busca.ids.id.text = ""
        self.ids.collect_page.ids.busca.ids.dose.text = ""
        self.ids.collect_page.ids.busca.ids.fabricante.text = ""




