from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkFont, CTkCheckBox, CTkImage
from arduino_communication import ArduinoCommunication
from tkinter import LEFT, RIGHT, BOTTOM, BOTH, IntVar
from request_alt import dict_to_list
from data_users import golgi_users
from CTkListbox.CTkListbox import *
from dataframe import *
from config import *
from PIL import Image
import time

class AddUser(CTkFrame):

    def submit_user(self):
        """Callback function to register new user in dataset

        Returns:
            bool: True if all fields were completed
        """
        self.nome = self.nameEntry.get()
        self.nusp = self.nuspEntry.get()
        self.rfid = self.rfidEntry.get()
        self.senha = self.passwordEntry.get()
        self.senha_verify = self.confirmpasswordEntry.get()
        self.is_new_user_admin = self.isAdm.get()
    

        if (self.nome == "" or self.nusp == "" or self.rfid == "" or self.senha == "" or self.senha_verify == ""):
            print("Complete form!\n")
            print(self.nome + "\n")
            print(self.nusp + "\n")
            print(self.rfid + "\n")
            print(self.senha + "\n")
            print(self.senha_verify + "\n")

            return False

        elif self.senha != self.senha_verify:
            print("Senha não corresponde! ")

        else:
            user =  [{
                "nusp": self.nusp,
                "nome": self.nome, 
                "rfid": self.rfid,
                "senha": self.senha,
                "admin": self.is_new_user_admin,
                }]
            
            golgi_users.add_user(user)
            golgi_users.save_to_disk()
            
            '''golgi_data.add_item(item)
            golgi_data.save_to_disk()
            self.ids.nome.text = ""
            self.ids.nusp.text = ""
            self.ids.dose.text = ""
            self.ids.apresentacao.text = ""
            self.ids.position.text = ""'''

            return True


    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        fr_add_user = CTkFrame(self, fg_color="transparent")
        fr_add_user.pack(expand=True, padx=10, pady=10)

        self.nameLabel = CTkLabel(fr_add_user, text="Nome", font=LARGE_FONT)
        self.nameLabel.grid(row=0, column=2, columnspan=2, sticky='w')

        self.nameEntry = CTkEntry(fr_add_user) 
        self.nameEntry.grid(row=1, column=2, columnspan=2, sticky='nsew')

        self.nuspLabel = CTkLabel(fr_add_user, text="NUSP", font=LARGE_FONT)
        self.nuspLabel.grid(row=2, column=2, columnspan=2, sticky='w')

        self.nuspEntry = CTkEntry(fr_add_user) 
        self.nuspEntry.grid(row=3, column=2, columnspan=2, sticky='nsew')

        self.rfidLabel = CTkLabel(fr_add_user, text="Card ID (RFID)", font=LARGE_FONT)
        self.rfidLabel.grid(row=4, column=2, columnspan=2, sticky='w')

        self.rfidEntry = CTkEntry(fr_add_user) 
        self.rfidEntry.grid(row=5, column=2, columnspan=2, sticky='nsew')

        self.passwordLabel = CTkLabel(fr_add_user, text="Senha", font=LARGE_FONT)
        self.passwordLabel.grid(row=6, column=2, columnspan=2, sticky='w')

        self.passwordEntry = CTkEntry(fr_add_user, show='*') 
        self.passwordEntry.grid(row=7, column=2, columnspan=2, sticky='nsew')
        
        self.confirmpasswordLabel = CTkLabel(fr_add_user, text="Confirmar Senha", font=LARGE_FONT)
        self.confirmpasswordLabel.grid(row=8, column=2, columnspan=2, sticky='w')

        self.confirmpasswordEntry = CTkEntry(fr_add_user, show='*') 
        self.confirmpasswordEntry.grid(row=9, column=2, columnspan=2, sticky='nsew')

        self.isAdm = IntVar()
        self.admBox = CTkCheckBox(fr_add_user, text = "Administrador(a)", variable=self.isAdm)
        self.admBox.grid(row=10, column=2, sticky='w', pady=10, padx=5)

        self.addButton = CTkButton(fr_add_user, text="Adicionar",
                            command=self.submit_user)
        self.addButton.grid(row=10, column=3)


class CollectInfo(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        fr_paciente = CTkFrame(self, fg_color="transparent")
        fr_paciente.pack(expand=True, padx=10, pady=10)

        self.pacienteLabel = CTkLabel(fr_paciente, text="Paciente", font=LARGE_FONT)
        self.pacienteLabel.grid(row=0, column=2, columnspan=2, sticky='w')

        self.pacienteEntry = CTkEntry(fr_paciente) 
        self.pacienteEntry.grid(row=1, column=2, columnspan=2, sticky='nsew')

        self.idLabel = CTkLabel(fr_paciente, text="ID", font=LARGE_FONT)
        self.idLabel.grid(row=2, column=2, columnspan=2, sticky='w')

        self.idEntry = CTkEntry(fr_paciente) 
        self.idEntry.grid(row=3, column=2, columnspan=2, sticky='nsew')

        self.submitButton = CTkButton(fr_paciente, text="Submit",
                            command=lambda: controller.show_frame(Collect))
        self.submitButton.grid(row=4, column=2, columnspan=2, pady=20) #button1

class Collect(CTkFrame):

    def display(self, event):

        index = self.listbox.curselection()
        selected = self.data.iloc[index]
        print(f"selected index: {index}:\n", selected)
        print(f"name {selected.nome}")

        self.id = selected.id
        self.nome = selected.nome
        self.dose = selected.dosagem
        self.apresentacao = selected.apresentacao
        self.estoque = selected.estoque

        if self.id in self.collect_list.keys():
            self.lbl_value["text"] = str(int(self.collect_list[self.id]))

        else:
            self.lbl_value["text"] = "0"

        self.stockLabel.configure(text=f'Quantidade disponível: {self.estoque}')

    # update listbox
    def update_listbox(self):
        self.listbox.delete("all")

        self.id = self.idEntry.get()
        self.nome = self.nameEntry.get()
        self.dose = self.doseEntry.get()
        self.apresentacao = self.presentationEntry.get()

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)

        print("oi:", self.data)

        for item in self.data.nome:
            self.listbox.insert("end", item, update = False)
        self.listbox.update();

        # for i in range(len(self.data.nome)-1):
        #     self.listbox.insert("end", self.data.nome[i])

    def increase(self):
        value = int(self.lbl_value.cget("text"))
        if value < int(self.estoque):
            self.lbl_value.configure(text=f"{value + 1}")

    def decrease(self):
        value = int(self.lbl_value.cget("text"))
        if value > 0:
            self.lbl_value.configure(text=f"{value - 1}")

    def add_to_queue(self):
        if self.listbox.get() is None:
            print("Escolha um medicamento!")
            return False
       
        elif int(self.lbl_value.cget("text")) == 0:
            print("Quantidade inválida!")

        else:
            self.collect_list[self.id] = int(self.lbl_value.cget("text"))
            # for i in range(int(self.lbl_value.cget("text"))):
            #     self.collect_list.put(self.id)
            self.listbox.selection_clear()
            #self.lbl_value["text"] = "0"

            #print(self.collect_list.queue)
            print(self.collect_list)
            

        return self.collect_list

    def collect(self):
        items = self.collect_list.items()
        for id, amount in items:
            golgi_data.update_amount(id, amount)
        
        queue = dict_to_list(self.collect_list)

        communication = ArduinoCommunication()
        connect = communication.connect(ESP_PORT)
        if connect:
            loading_img = CTkImage(light_image=Image.open("images/icon-logo-gradient.png"))#placeholder de imagem (?) do golgi
            self.loading_txt = CTkLabel(self, bg_color="gray26", width=100, height=10, text="Por favor, espere enquanto o Golgi coleta o(s) remedio(s)", font=("Verdana", 18))
            self.loading_txt.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.5)
            self.loading_img = CTkLabel(self, bg_color="gray26", width=100, height=10, text="ahhh", image=loading_img)
            self.loading_img.place(relx=0.1, rely=0.3, relwidth=0.1, relheight=0.5)
            self.update()
            for item in queue:
                item = bytes(str(item), encoding='utf-8')
                communication.send_message(item)
                time.sleep(2)
            self.loading_txt.destroy()
            self.loading_img.destroy()
        
        self.stockLabel.configure(text='')

        return True
        

    def __init__(self, parent, controller):

        CTkFrame.__init__(self, parent)

        self.collect_list = {}

        fr_collect_data = CTkFrame(self, fg_color="transparent")
        fr_collect_data.pack(fill="both", expand=True, padx=10, pady=10)

        # search data
        fr_data = CTkFrame(fr_collect_data, fg_color="transparent")
        fr_data.pack(padx=10, pady=10, side=LEFT)

        # 'Nome' entry 1
        self.nameEntry = CTkEntry(fr_data, placeholder_text="Nome") 
        self.nameEntry.pack(padx=5, pady=10)
        self.nameEntry.bind('<Return>', (lambda func : print(self.update_listbox())))

        # 'ID' entry 2
        self.idEntry = CTkEntry(fr_data, placeholder_text="ID") 
        self.idEntry.pack(padx=5, pady=10)
        self.idEntry.bind('<Return>', (lambda func : print(self.update_listbox())))

        # 'Dosagem' entry 3
        self.doseEntry = CTkEntry(fr_data, placeholder_text="Dosagem") 
        self.doseEntry.pack(padx=5, pady=10);

        # 'Apresentação' entry 4
        self.presentationEntry = CTkEntry(fr_data, placeholder_text="Apresentação") 
        self.presentationEntry.pack(padx=5, pady=10)
        
        # search result
        fr_listbox = CTkFrame(fr_collect_data)
        fr_listbox.pack(fill="both", expand=True, side=LEFT)

        # self.listbox = tk.Listbox(fr_listbox, width=55)
        # self.listbox.pack(fill="both", expand=True)

        self.listbox = CTkListbox(fr_listbox, width=55)
        self.listbox.pack(fill="both", expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.display)

        # fix bug scroll on linux
        self.listbox.bind_all("<Button-4>", lambda e: self.listbox._parent_canvas.yview("scroll", -1, "units"))
        self.listbox.bind_all("<Button-5>", lambda e: self.listbox._parent_canvas.yview("scroll", 1, "units"))

        # stock
        fr_stock = CTkFrame(fr_collect_data, fg_color="transparent")
        fr_stock.pack(padx=10, pady=10, side=LEFT)

        self.stockLabel = CTkLabel(fr_stock, text='', font=FONT)
        self.stockLabel.grid(padx=0, pady=5, row=0, column=0, columnspan=3, sticky='w')

        fr_qtd = CTkFrame(fr_stock, fg_color="transparent")
        fr_qtd.grid(padx=0, pady=5, row=1, column=0, columnspan=3)

        self.btn_decrease = CTkButton(fr_qtd, text="-", width=30, command=self.decrease)
        self.btn_decrease.grid(padx=0, pady=5, row=0, column=0, sticky='w')

        self.lbl_value = CTkLabel(fr_qtd, text="0", font=FONT)
        self.lbl_value.grid(padx=0, pady=5, row=0, column=1)

        self.btn_increase = CTkButton(fr_qtd, text="+", width=30, command=self.increase)
        self.btn_increase.grid(padx=0, pady=5, row=0, column=2, sticky='e')

        self.add_button = CTkButton(fr_qtd, text="Adicionar", command=self.add_to_queue)
        self.add_button.grid(padx=0, pady=5, row=1, column=0, columnspan=3)

        # search and collect buttons
        fr_search_collect = CTkFrame(self, fg_color="transparent")
        fr_search_collect.pack(padx=10, pady=10)

        self.searchButton = CTkButton(fr_search_collect, text="Pesquisar", command=self.update_listbox)
        self.searchButton.pack(padx=10, pady=5, side=LEFT)

        self.collectButton = CTkButton(fr_search_collect, text="Coletar", command=self.collect)
        self.collectButton.pack(padx=10, pady=5, side=RIGHT)
        
        # menu
        #self.menu = Menu(self, controller)
        #self.menu.disable_collect()
        #self.menu.pack()

class Config(CTkFrame):

    def logout(self, controller):
        controller.show_frame(StartPage)

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        fr_config = CTkFrame(self, fg_color="transparent")
        fr_config.pack(expand=True, padx=10, pady=10)

        # 'Log-in' button 
        self.logoutButton = CTkButton(fr_config, text='Log-out', command=lambda: self.logout(controller))
        self.logoutButton.pack(padx=10, pady=10)

class Delete(CTkFrame):

    # update listbox
    def update_listbox(self):
        self.listbox.delete(0, "end")

        self.id = self.idEntry.get()
        self.nome = self.nameEntry.get()
        self.dose = self.doseEntry.get()
        self.apresentacao = self.presentationEntry.get()
        self.posicao = self.positionEntry.get()

        if self.id == "ID":
            self.id = ""

        if self.nome == "Nome":
            self.nome = ""

        if self.dose == "Dose":
            self.dose = ""

        if self.apresentacao == "Apresentação":
            self.apresentacao = ""

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)

        for item in self.data.nome:
            self.listbox.insert("end", item)

        # for i in range(len(self.data.nome)-1):
        #     self.listbox.insert("end", self.data.nome[i])



    def delete(self):
        """Callback function to delete registered item

        Returns:
            bool: True if all fields are completed
        """
        self.id = ""
        self.dose = ""
        self.apresentacao = ""
        self.nome = self.listbox.get()

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)
        self.data = self.data.reset_index()

        self.id = self.data.id[0]
        self.nome = self.data.nome[0]
        self.dose = self.data.dosagem[0]
        self.apresentacao = self.data.apresentacao[0]
        self.position = self.data.position[0]


        golgi_data.delete_item(self.id)#int(float(item.id)))
        golgi_data.save_to_disk()

        self.idEntry.delete(0, "end")
        self.nameEntry.delete(0, "end")
        self.doseEntry.delete(0, "end")
        self.presentationEntry.delete(0, "end")
        self.positionEntry.delete(0, "end")

        self.idEntry.insert(0, "ID")
        self.nameEntry.insert(0, "Nome")
        self.doseEntry.insert(0, "Dosagem")
        self.presentationEntry.insert(0, "Apresentação")
        self.positionEntry.insert(0, "Posição")


    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        fr_delete = CTkFrame(self, fg_color="transparent")
        fr_delete.pack(fill="both", expand=True, padx=10, pady=10)

        # search data
        fr_data = CTkFrame(fr_delete, fg_color="transparent")
        fr_data.pack(padx=10, pady=10, side=LEFT)

        # 'Nome' entry 1
        self.nameEntry = CTkEntry(fr_data, placeholder_text="Nome") 
        self.nameEntry.pack(padx=5, pady=10)

        # 'ID' entry 2
        self.idEntry = CTkEntry(fr_data, placeholder_text="ID") 
        self.idEntry.pack(padx=5, pady=10)

        # 'Dosagem' entry 3
        self.doseEntry = CTkEntry(fr_data, placeholder_text="Dosagem") 
        self.doseEntry.pack(padx=5, pady=10);

        # 'Apresentação' entry 4
        self.presentationEntry = CTkEntry(fr_data, placeholder_text="Apresentação") 
        self.presentationEntry.pack(padx=5, pady=10)

        # 'Position' entry
        self.positionEntry = CTkEntry(fr_data, placeholder_text="Posição") 
        self.positionEntry.pack(padx=5, pady=10)

        fr_listbox = CTkFrame(fr_delete)
        fr_listbox.pack(fill="both", expand=True, padx=10, pady=0, side=LEFT)

        self.listbox = CTkListbox(fr_listbox, width=60)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=0)

        #self.listbox.bind("<<ListboxSelect>>", self.edit)

        fr_search_delete = CTkFrame(self, fg_color="transparent")
        fr_search_delete.pack(padx=10, pady=5)

        self.searchButton = CTkButton(fr_search_delete, text="Pesquisar", command=self.update_listbox)
        self.searchButton.pack(padx=10, pady=5, side=LEFT)

        self.deleteButton = CTkButton(fr_search_delete, text="Confirm Delete", command=self.delete)
        self.deleteButton.pack(padx=10, pady=5, side=LEFT)

class Edit(CTkFrame):

    def edit(self, event):
        self.idEntry.delete(0, "end")
        self.nameEntry.delete(0, "end")
        self.doseEntry.delete(0, "end")
        self.presentationEntry.delete(0, "end")
        self.positionEntry.delete(0, "end")

        self.id = ""
        self.dose = ""
        self.apresentacao = ""
        self.nome = self.listbox.get()
        #self.nome = self.listbox.get(self.listbox.curselection())
        
        #print(self.nome)

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)
        self.data = self.data.reset_index()

        self.id = self.data.id[0]
        self.nome = self.data.nome[0]
        self.dose = self.data.dosagem[0]
        self.apresentacao = self.data.apresentacao[0]
        self.position = self.data.position[0]

        #print(self.id, self.nome, self.dose, self.apresentacao, self.position)

        self.idEntry.insert(0, str(self.id))
        self.nameEntry.insert(0, str(self.nome))
        self.doseEntry.insert(0, str(self.dose))
        self.presentationEntry.insert(0, str(self.apresentacao))
        self.positionEntry.insert(0, str(self.position))


    # update listbox
    def update_listbox(self):
        self.listbox.delete(0, "end")

        self.id = self.idEntry.get()
        self.nome = self.nameEntry.get()
        self.dose = self.doseEntry.get()
        self.apresentacao = self.presentationEntry.get()
        self.posicao = self.positionEntry.get()

        if self.id == "ID":
            self.id = ""

        if self.nome == "Nome":
            self.nome = ""

        if self.dose == "Dose":
            self.dose = ""

        if self.apresentacao == "Apresentação":
            self.apresentacao = ""

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)

        for item in self.data.nome:
            self.listbox.insert("end", item)

        # for i in range(len(self.data.nome)-1):
        #     self.listbox.insert("end", self.data.nome[i])



    def submit_item(self):
        """Callback function to register edited item

        Returns:
            bool: True if all fields are completed
        """
        self.id = self.idEntry.get()
        self.nome = self.nameEntry.get()
        self.dose = self.doseEntry.get()
        self.apresentacao = self.presentationEntry.get()
        self.position = self.positionEntry.get()

        print(self.id, self.nome, self.dose, self.apresentacao, self.position)

        if (self.nome == "" or self.id == "" or self.dose == "" or self.apresentacao == "" or self.position == ""):
            print("Complete form!\n")
            print(self.nome + "\n")
            print(self.id + "\n")
            print(self.position + "\n")
            print(self.dose + "\n")
            print(self.apresentacao + "\n")
            return False
        else:
            item =  [{
                "id": self.id,
                "nome": self.nome, 
                "dosagem": self.dose,
                "apresentacao": self.apresentacao,
                "position": self.position,
                }]

            print(item)

            golgi_data.modify_item(self.id, item)
            golgi_data.save_to_disk()
            self.idEntry.delete(0, "end")
            self.nameEntry.delete(0, "end")
            self.doseEntry.delete(0, "end")
            self.presentationEntry.delete(0, "end")
            self.positionEntry.delete(0, "end")

            self.idEntry.insert(0, "ID")
            self.nameEntry.insert(0, "Nome")
            self.doseEntry.insert(0, "Dosagem")
            self.presentationEntry.insert(0, "Apresentação")
            self.positionEntry.insert(0, "Posição")


            return True


    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        fr_edit = CTkFrame(self, fg_color="transparent")
        fr_edit.pack(fill="both", expand=True, padx=10, pady=10)

        # search data
        fr_data = CTkFrame(fr_edit, fg_color="transparent")
        fr_data.pack(padx=10, pady=10, side=LEFT)

        # 'Nome' entry 1
        self.nameEntry = CTkEntry(fr_data, placeholder_text="Nome") 
        self.nameEntry.pack(padx=5, pady=10)

        # 'ID' entry 2
        self.idEntry = CTkEntry(fr_data, placeholder_text="ID") 
        self.idEntry.pack(padx=5, pady=10)

        # 'Dosagem' entry 3
        self.doseEntry = CTkEntry(fr_data, placeholder_text="Dosagem") 
        self.doseEntry.pack(padx=5, pady=10);

        # 'Apresentação' entry 4
        self.presentationEntry = CTkEntry(fr_data, placeholder_text="Apresentação") 
        self.presentationEntry.pack(padx=5, pady=10)

        # 'Position' entry
        self.positionEntry = CTkEntry(fr_data, placeholder_text="Posição") 
        self.positionEntry.pack(padx=5, pady=10)

        fr_listbox = CTkFrame(fr_edit)
        fr_listbox.pack(fill="both", expand=True, padx=10, pady=0, side=LEFT)

        self.listbox = CTkListbox(fr_listbox, width=60)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=0)
        self.listbox.bind("<<ListboxSelect>>", self.edit)

        # fix bug scroll on linux
        self.listbox.bind_all("<Button-4>", lambda e: self.listbox._parent_canvas.yview("scroll", -1, "units"))
        self.listbox.bind_all("<Button-5>", lambda e: self.listbox._parent_canvas.yview("scroll", 1, "units"))

        fr_search_edit = CTkFrame(self, fg_color="transparent")
        fr_search_edit.pack(padx=10, pady=5)

        self.searchButton = CTkButton(fr_search_edit, text="Pesquisar", command=self.update_listbox)
        self.searchButton.pack(padx=10, pady=5, side=LEFT)

        self.editButton = CTkButton(fr_search_edit, text="Confirm Edit", command=self.submit_item)
        self.editButton.pack(padx=10, pady=5, side=LEFT)

class Menu(CTkFrame):

    def __init__(self, parent, page, controller):
        super().__init__(parent, fg_color="transparent")

        fr_menu = CTkFrame(self, fg_color="transparent")
        fr_menu.pack(padx=10, pady=10)

        self.collectMenu = CTkButton(fr_menu, text="Coletar", 
                            command=lambda: controller.show_frame(CollectInfo))

        self.collectMenu.pack(padx=5, pady=10, side=LEFT)

        self.registerMenu = CTkButton(fr_menu, text="Registrar",
                            command=lambda: controller.show_frame(Register))
        self.registerMenu.pack(padx=5, pady=10, side=LEFT)

        self.editMenu = CTkButton(fr_menu, text="Editar",
                            command=lambda: controller.show_frame(Edit))
        self.editMenu.pack(padx=5, pady=10, side=LEFT)
        self.deleteMenu = CTkButton(fr_menu, text="Apagar",
                            command=lambda: controller.show_frame(Delete))
        self.deleteMenu.pack(padx=5, pady=10, side=LEFT)
        self.addUserMenu = CTkButton(fr_menu, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.addUserMenu.pack(padx=5, pady=10, side=LEFT)
        self.settingsMenu = CTkButton(fr_menu, text="Configurações",
                            command=lambda: controller.show_frame(Config))
        self.settingsMenu.pack(padx=5, pady=10, side=LEFT)

        if (page == CollectInfo):
            self.collectMenu.configure(state="disabled")
        elif (page == Register):
            self.registerMenu.configure(state="disabled")
        elif (page == Edit):
            self.editMenu.configure(state="disabled")
        elif (page == Delete):
            self.deleteMenu.configure(state="disabled")
        elif (page == AddUser):
            self.addUserMenu.configure(state="disabled")
        elif (page == Config):
            self.settingsMenu.configure(state="disabled")

    def disable_collect(self):
        self.collectMenu.configure(state="disabled")

class Register(CTkFrame):

    def submit_item(self):
        """Callback function to register new item in dataset

        Returns:
            bool: True if all fields were completed
        """
        self.id = self.idEntry.get()
        self.nome = self.nameEntry.get()
        self.dose = self.doseEntry.get()
        self.apresentacao = self.presentationEntry.get()
        self.position = self.positionEntry.get()
    
        name_ver = self.nome == "" or self.nome == "Nome"
        id_ver = self.id == "" or self.id == "ID"
        dose_ver = self.dose == "" or self.dose == "Dosagem"
        present_ver = self.apresentacao == "" or self.apresentacao == "Apresentação"
        position_ver = self.position == "" or self.position == "Posição"
        
        if (name_ver and id_ver and dose_ver and present_ver and position_ver):
        # if (self.nome == "" or self.id == "" or self.dose == "" or self.apresentacao == "" or self.position == ""):
            print("Complete form!\n")
            print(self.nome + "\n")
            print(self.id + "\n")
            print(self.position + "\n")
            print(self.dose + "\n")
            print(self.apresentacao + "\n")

            return False
        else:
            
            item =  [{
                "id": self.id,
                "nome": self.nome, 
                "dosagem": self.dose,
                "apresentacao": self.apresentacao,
                "position": self.position,
                }]
            golgi_data.add_item(item)
            golgi_data.save_to_disk()

            self.idEntry.delete(0, "end")
            self.nameEntry.delete(0, "end")
            self.doseEntry.delete(0, "end")
            self.presentationEntry.delete(0, "end")
            self.positionEntry.delete(0, "end")

            self.idEntry.insert(0, "ID")
            self.nameEntry.insert(0, "Nome")
            self.doseEntry.insert(0, "Dosagem")
            self.presentationEntry.insert(0, "Apresentação")
            self.positionEntry.insert(0, "Posição")

            return True

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        
        fr_register = CTkFrame(self, fg_color="transparent")
        fr_register.pack(expand=True, padx=10, pady=10)

        # 'Nome' entry
        self.nameEntry = CTkEntry(fr_register, placeholder_text="Nome") 
        self.nameEntry.pack(padx=10, pady=10)

        # 'ID' entry
        self.idEntry = CTkEntry(fr_register, placeholder_text="ID") 
        self.idEntry.pack(padx=10, pady=10)

        # 'Dosagem' entry
        self.doseEntry = CTkEntry(fr_register, placeholder_text="Dosagem") 
        self.doseEntry.pack(padx=10, pady=10)

        # 'Apresentação' entry
        self.presentationEntry = CTkEntry(fr_register, placeholder_text="Apresentação") 
        self.presentationEntry.pack(padx=10, pady=10)

        # 'Position' entry
        self.positionEntry = CTkEntry(fr_register, placeholder_text="Posição") 
        self.positionEntry.pack(padx=10, pady=10)

        self.registerButton = CTkButton(fr_register, text="Registrar",
                            command=lambda: self.submit_item())
        self.registerButton.pack(padx=10, pady=10)

class ResetPassword(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        fr_reset = CTkFrame(self, fg_color="transparent")
        fr_reset.pack(expand=True, padx=10, pady=10)

        self.label = CTkLabel(fr_reset, text="Esqueci minha senha", font=CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        self.infoLabel = CTkLabel(fr_reset, text="Por favor, entre em contato com a organização\npor meio do número: (99) 99999-9999", font=FONT)
        self.infoLabel.pack(pady=20)

        self.menuButton = CTkButton(fr_reset, text="Retornar ao menu principal", font=FONT,
                            command=lambda: controller.show_frame(StartPage))
        self.menuButton.pack(pady=20)

class StartPage(CTkFrame):

    def login(self, controller):
        #add popup if wrong password
        user = self.userEntry.get() 
        password = self.passwordEntry.get();
        checker = golgi_users.validate(user, password)
        adm = golgi_users.get_admin(user)

        if checker:
            self.userEntry.delete(0, "end")
            self.passwordEntry.delete(0, "end")
            controller.show_frame(CollectInfo)

        return adm

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        fr_login = CTkFrame(self, fg_color="transparent")
        fr_login.pack(expand=True, padx=10, pady=10)

        # 'Usuário' label
        self.userLabel = CTkLabel(fr_login, text='Usuário: ', font=FONT)
        self.userLabel.pack(padx=5, pady=5)

        # 'Usuário' entry
        self.userEntry = CTkEntry(fr_login, font=FONT) 
        self.userEntry.pack(padx=5, pady=5)
        self.userEntry.bind('<Return>', (lambda func : self.login(controller)))

        # 'Senha' label
        self.passwordLabel = CTkLabel(fr_login, text='Senha: ', font=FONT)
        self.passwordLabel.pack(padx=5, pady=5)

        # 'Senha' entry
        self.passwordEntry = CTkEntry(fr_login, show="*", font=FONT) 
        self.passwordEntry.pack(padx=5, pady=5)
        self.passwordEntry.bind('<Return>', (lambda func : self.login(controller)))

        # 'Entrar' button 
        self.loginButton = CTkButton(fr_login, text='Entrar', font=FONT, command=lambda: self.login(controller))
        self.loginButton.pack(padx=5, pady=(25, 5))

        # 'Esqueci minha senha' button
        self.forgotButton = CTkButton(fr_login, text='Esqueci minha senha', font=FONT, command= lambda: reset_password(controller))
        self.forgotButton.pack(padx=5, pady=10)
