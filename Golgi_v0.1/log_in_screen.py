from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

class LogInPage(MDBoxLayout):
    """Log In page declaration

    Args:
        MDBoxLayout: BoxLayout from KivyMD
    """
    pass

class ActualLogIn(MDBoxLayout):
    def on_login(self):
        app= MDApp.get_running_app()
        
        if self.ids.user.text == 'admin':
            app.root.current = "admin_main_screen"
        else:
            app.root.current = "main_screen"