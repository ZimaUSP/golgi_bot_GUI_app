from kivymd.uix.boxlayout import MDBoxLayout



class Resultado(MDBoxLayout):
    """Each individual search result layout

    Args:
        MDBoxLayout: BoxLayout from MDKivy
    """

    def __init__(self):
        """Initialisation method
        """
        self.nome = "Nome!"
        self.id = "0"
        self.dose = "Dosagem!"
        self.apresentacao = "apresentacao!"
        self.position = ""
        
        
    def generate(self, **kwargs):
        """Generates the actual widget
        """
        super().__init__(**kwargs)

    def set_nome(self, nome):
        """Set the name on search item

        Args:
            nome (str): The name

        Returns:
            [bool]: true if a string is passed as parameter
        """
        if (isinstance(nome, str)):
            self.nome = nome
            return True
        return False
    
    def set_id(self, id):
        """Set the ID on search item

        Args:
            id (str): the unique identification of item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(id, str)):
            self.id = id
            return True
        return False

    def set_dose(self, dose):
        """Set the dose on search item

        Args:
            dose (str): dose of the item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(dose, str)):
            self.dose = dose
            return True
        return False

    def set_apresentacao(self, apresentacao):
        """Set the manufacturer on search item

        Args:
            apresentacao ([str): manufactorer of the item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(apresentacao, str)):
            self.apresentacao = apresentacao
            return True
        return False


    def set_position(self, position):
        """Set the position of search item

        Args:
            position (str): position on robot of the item

        Returns:
            [bool]: true if a string is passed
        """
        if (isinstance(position, str)):
            self.position = position
            return True
        return False

        

class ResultadoMultiplo(Resultado):
    pass


    
class ResultadoBinario(Resultado):
    pass


class Contador(MDBoxLayout):
    def __init__(self, **kwargs):
        self.quantity = 0
        super().__init__(**kwargs)
    
    def on_plus(self):
        self.quantity +=1
        self.ids.number.text = str(self.quantity)
        pass

    def on_minus(self):
        if (self.quantity <= 0):
            pass
        else:
            self.quantity -= 1
            self.ids.number.text = str(self.quantity)
        pass
   