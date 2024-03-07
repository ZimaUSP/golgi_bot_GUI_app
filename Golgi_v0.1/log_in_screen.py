from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from data_users import *

class LogInPage(MDBoxLayout):
    """Log In page declaration

    Args:
        MDBoxLayout: BoxLayout from KivyMD
    """
    pass

class ActualLogIn(MDBoxLayout):
    def on_login(self):
        app= MDApp.get_running_app()
        
        checker = golgi_users.validate(self.ids.user.text, self.ids.password.text)
        adm = golgi_users.get_admin(self.ids.user.text)
        
        if checker:
            if adm:
                app.root.current = "admin_main_screen"
            else:
                app.root.current = "main_screen"
        '''
        if self.ids.user.text == 'admin':
            app.root.current = "admin_main_screen"
        else:
            app.root.current = "main_screen"
        '''