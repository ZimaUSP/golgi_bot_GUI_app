from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout


class MainPage(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_collect_enter(self):
        self.ids.collect_page.ids.busca.ids.nome.text = ""
        self.ids.collect_page.ids.busca.ids.id.text = ""
        self.ids.collect_page.ids.busca.ids.dose.text = ""
        self.ids.collect_page.ids.busca.ids.fabricante.text = ""




