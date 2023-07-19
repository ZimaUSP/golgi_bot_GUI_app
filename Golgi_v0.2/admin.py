import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from data_users import golgi_users
from dataframe import *
from math import ceil
from queue import Queue
from request_alt import dict_to_list, communication

LARGE_FONT= ("Verdana", 12)

FONT = ('Helvetica', 14)

# Define button functions
def reset_password(controller):
    controller.show_frame(ResetPassword)
    return

def login(user, password, controller):
    #add popup if wrong password
    checker = golgi_users.validate(user, password)
    adm = golgi_users.get_admin(user)

    if checker:
        controller.show_frame(AdminCollect1)

    return adm

class StartPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        # 'Usuário' label
        self.userLabel = ctk.CTkLabel(self, text='Usuário: ', font=FONT)
        self.userLabel.pack()

        # 'Usuário' entry
        self.userEntry = ctk.CTkEntry(self, font=FONT) 
        self.userEntry.pack()
        self.userEntry.delete(0)

        # Empty label, skip line
        self.emptyLabel = ctk.CTkLabel(self, text=' ')
        self.emptyLabel.pack()

        # 'Senha' label
        self.passwordLabel = ctk.CTkLabel(self, text='Senha: ', font=FONT)
        self.passwordLabel.pack()

        # 'Senha' entry
        self.passwordEntry = ctk.CTkEntry(self, show="*", font=FONT) 
        self.passwordEntry.pack()

        self.passwordEntry.bind('<Return>', (lambda func : login(self.userEntry.get(), self.passwordEntry.get(), controller)))

        # Empty label, skip line
        self.emptyLabel2 = ctk.CTkLabel(self, text=' ')
        self.emptyLabel2.pack()

        # 'Entrar' button 
        self.loginButton = ctk.CTkButton(self, text='Entrar', font=FONT, command=lambda: login(self.userEntry.get(), self.passwordEntry.get(), controller))
        self.loginButton.pack(pady=10)

        # 'Esqueci minha senha' button
        self.forgotButton = ctk.CTkButton(self, text='Esqueci minha senha', font=FONT, command= lambda: reset_password(controller))
        self.forgotButton.pack()


class ResetPassword(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.label = ctk.CTkLabel(self, text="Esqueci minha senha", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        self.infoLabel = ctk.CTkLabel(self, text="Por favor, entre em contato com a organização\npor meio do número: (99) 99999-9999", font=FONT)
        self.infoLabel.pack(pady=20)

        self.menuButton = ctk.CTkButton(self, text="Retornar ao menu principal", font=FONT,
                            command=lambda: controller.show_frame(StartPage))
        self.menuButton.pack(pady=20)

class AdminCollect1(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.pacienteLabel = ctk.CTkLabel(self, text="Paciente", font=LARGE_FONT)
        self.pacienteLabel.grid(row=0, column=2, columnspan=2, sticky='w')

        self.pacienteEntry = ctk.CTkEntry(self) 
        self.pacienteEntry.grid(row=1, column=2, columnspan=2, sticky='nsew')

        self.idLabel = ctk.CTkLabel(self, text="ID", font=LARGE_FONT)
        self.idLabel.grid(row=2, column=2, columnspan=2, sticky='w')

        self.idEntry = ctk.CTkEntry(self) 
        self.idEntry.grid(row=3, column=2, columnspan=2, sticky='nsew')

        self.submitButton = ctk.CTkButton(self, text="Submit",
                            command=lambda: controller.show_frame(AdminCollect2))
        self.submitButton.grid(row=4, column=2, columnspan=2, pady=20) #button1

        self.collectMenu = ctk.CTkButton(self, text="Coletar", state='disabled')
        self.collectMenu.grid(row=5, column=0) #button3

        self.registerMenu = ctk.CTkButton(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.registerMenu.grid(row=5, column=1) #button4

        self.editMenu = ctk.CTkButton(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.editMenu.grid(row=5, column=2) #button5

        self.deleteMenu = ctk.CTkButton(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.deleteMenu.grid(row=5, column=3) #button6


        self.addUserMenu = ctk.CTkButton(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.addUserMenu.grid(row=5, column=4) #button7

        self.settingsMenu = ctk.CTkButton(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.settingsMenu.grid(row=5, column=5) #button8


class AdminCollect2(ctk.CTkFrame):

    def display(self, event):
        self.idEntry.delete(0, "end")
        self.nameEntry.delete(0, "end")
        self.doseEntry.delete(0, "end")
        self.presentationEntry.delete(0, "end")
        #self.entry5.delete(0, "end")

        self.id = ""
        self.dose = ""
        self.apresentacao = ""
        self.nome = self.listbox.get("anchor")
        #self.nome = self.listbox.get(self.listbox.curselection())

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)
        self.data = self.data.reset_index()

        self.id = self.data.id[0]
        self.nome = self.data.nome[0]
        self.dose = self.data.dosagem[0]
        self.apresentacao = self.data.apresentacao[0]
        #self.position = self.data.position[0]

        self.idEntry.insert(0, str(self.id))
        self.nameEntry.insert(0, str(self.nome))
        self.doseEntry.insert(0, str(self.dose))
        self.presentationEntry.insert(0, str(self.apresentacao))
        #self.entry5.insert(0, str(self.position))

        if self.id in self.collect_list.keys():
            self.lbl_value["text"] = str(int(self.collect_list[self.id]))

        else:
            self.lbl_value["text"] = "0"

    # update listbox
    def update_listbox(self):
        self.listbox.delete(0, "end")

        self.id = self.idEntry.get()
        self.nome = self.nameEntry.get()
        self.dose = self.doseEntry.get()
        self.apresentacao = self.presentationEntry.get()

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

    def increase(self):
        value = int(self.lbl_value.cget("text"))
        self.lbl_value.configure(text=f"{value + 1}")

    def decrease(self):
        value = int(self.lbl_value.cget("text"))
        if value > 0:
            self.lbl_value.configure(text=f"{value - 1}")

    def add_to_queue(self):
        if self.listbox.get("anchor") is None:
            print("Escolha um medicamento!")
            return False
        
        elif int(self.lbl_value.cget("text")) == 0:
            print("Quantidade inválida!")

        else:
            self.collect_list[self.id] = int(self.lbl_value.cget("text"))
            # for i in range(int(self.lbl_value.cget("text"))):
            #     self.collect_list.put(self.id)
            self.listbox.selection_clear(0, "end")
            #self.lbl_value["text"] = "0"

            #print(self.collect_list.queue)
            print(self.collect_list)
            

        return self.collect_list

    def collect(self):
        queue = dict_to_list(self.collect_list)
        communication(queue)

        return True
        

    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)

        self.collect_list = {}

        # 'Nome' entry 1
        self.nameEntry = ctk.CTkEntry(self) 
        self.nameEntry.insert(0, "Nome")
        self.nameEntry.grid(row=0, column=0, columnspan=5, sticky='w')

        # 'ID' entry 2
        self.idEntry = ctk.CTkEntry(self) 
        self.idEntry.insert(0, "ID")
        self.idEntry.grid(row=1, column=0, columnspan=5, sticky='w')

        # 'Dosagem' entry 3
        self.doseEntry = ctk.CTkEntry(self) 
        self.doseEntry.insert(0, "Dosagem")
        self.doseEntry.grid(row=2, column=0, columnspan=5, sticky='w')

        # 'Apresentação' entry 4
        self.presentationEntry = ctk.CTkEntry(self) 
        self.presentationEntry.insert(0, "Apresentação")
        self.presentationEntry.grid(row=3, column=0, columnspan=5, sticky='w')

        self.searchButton = ctk.CTkButton(self, text="Pesquisar",
                            command=self.update_listbox)
        self.searchButton.grid(row=5, column=1, columnspan=2, pady=10)

        self.collectButton = ctk.CTkButton(self, text="Coletar", command=self.collect)
        self.collectButton.grid(row=5, column=3, columnspan=2)

        self.listbox = tk.Listbox(self, width=60)
        self.listbox.grid(row=0, column=1, columnspan=4, rowspan=4, sticky='w', padx=10)

        self.listbox.bind("<<ListboxSelect>>", self.display)

        self.btn_decrease = ctk.CTkButton(master=self, text="-", width=15, command=self.decrease)
        self.btn_decrease.grid(row=2, column=4, sticky='w')

        self.lbl_value = ctk.CTkLabel(master=self, text="0", font=FONT)
        self.lbl_value.grid(row=2, column=4)

        self.btn_increase = ctk.CTkButton(master=self, text="+", width=15, command=self.increase)
        self.btn_increase.grid(row=2, column=4, sticky='e')

        self.add_button = ctk.CTkButton(self, text="Adicionar", command=self.add_to_queue)
        self.add_button.grid(row=3, column=4)

        self.collectMenu = ctk.CTkButton(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.collectMenu.grid(row=6, column=0)

        self.registerMenu = ctk.CTkButton(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.registerMenu.grid(row=6, column=1) #button4

        self.editMenu = ctk.CTkButton(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.editMenu.grid(row=6, column=2) #button5

        self.deleteMenu = ctk.CTkButton(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.deleteMenu.grid(row=6, column=3) #button6

        self.addUserMenu = ctk.CTkButton(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.addUserMenu.grid(row=6, column=4) #button7

        self.settingsMenu = ctk.CTkButton(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.settingsMenu.grid(row=6, column=5) #button8

class AdminRegister(ctk.CTkFrame):

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
        ctk.CTkFrame.__init__(self, parent)

        

        # 'Nome' entry
        self.nameEntry = ctk.CTkEntry(self) 
        self.nameEntry.insert(0, "Nome")
        self.nameEntry.grid(row=0, column=0, columnspan=5, sticky='w')

        # 'ID' entry
        self.idEntry = ctk.CTkEntry(self) 
        self.idEntry.insert(0, "ID")
        self.idEntry.grid(row=1, column=0, columnspan=5, sticky='w')

        # 'Dosagem' entry
        self.doseEntry = ctk.CTkEntry(self) 
        self.doseEntry.insert(0, "Dosagem")
        self.doseEntry.grid(row=2, column=0, columnspan=5, sticky='w')

        # 'Apresentação' entry
        self.presentationEntry = ctk.CTkEntry(self) 
        self.presentationEntry.insert(0, "Apresentação")
        self.presentationEntry.grid(row=3, column=0, columnspan=5, sticky='w')

        # 'Position' entry
        self.positionEntry = ctk.CTkEntry(self) 
        self.positionEntry.insert(0, "Posição")
        self.positionEntry.grid(row=4, column=0, columnspan=5, sticky='w')

        self.registerButton = ctk.CTkButton(self, text="Registrar",
                            command=lambda: self.submit_item())
        self.registerButton.grid(row=5, column=0, columnspan=3)

        self.collectMenu = ctk.CTkButton(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.collectMenu.grid(row=6, column=0)

        self.registerMenu = ctk.CTkButton(self, text="Registrar", state='disabled')
        self.registerMenu.grid(row=6, column=1) #button4

        self.editMenu = ctk.CTkButton(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.editMenu.grid(row=6, column=2) #button5

        self.deleteMenu = ctk.CTkButton(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.deleteMenu.grid(row=6, column=3) #button6

        self.addUserMenu = ctk.CTkButton(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.addUserMenu.grid(row=6, column=4) #button7

        self.settingsMenu = ctk.CTkButton(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.settingsMenu.grid(row=6, column=5) #button8
        

class AdminEdit(ctk.CTkFrame):

    def edit(self, event):
        self.idEntry.delete(0, "end")
        self.nameEntry.delete(0, "end")
        self.doseEntry.delete(0, "end")
        self.presentationEntry.delete(0, "end")
        self.positionEntry.delete(0, "end")

        self.id = ""
        self.dose = ""
        self.apresentacao = ""
        self.nome = self.listbox.get("anchor")
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
        ctk.CTkFrame.__init__(self, parent)

        # 'Nome' entry
        self.nameEntry = ctk.CTkEntry(self) 
        self.nameEntry.insert(0, "Nome")
        self.nameEntry.grid(row=0, column=0, columnspan=5, sticky='w')

        # 'ID' entry
        self.idEntry = ctk.CTkEntry(self) 
        self.idEntry.insert(0, "ID")
        self.idEntry.grid(row=1, column=0, columnspan=5, sticky='w')

        # 'Dosagem' entry
        self.doseEntry = ctk.CTkEntry(self) 
        self.doseEntry.insert(0, "Dosagem")
        self.doseEntry.grid(row=2, column=0, columnspan=5, sticky='w')

        # 'Apresentação' entry
        self.presentationEntry = ctk.CTkEntry(self) 
        self.presentationEntry.insert(0, "Apresentação")
        self.presentationEntry.grid(row=3, column=0, columnspan=5, sticky='w')

        # 'Position' entry
        self.positionEntry = ctk.CTkEntry(self) 
        self.positionEntry.insert(0, "Posição")
        self.positionEntry.grid(row=4, column=0, columnspan=5, sticky='w')

        self.searchButton = ctk.CTkButton(self, text="Pesquisar",
                            command=self.update_listbox)
        self.searchButton.grid(row=5, column=1, columnspan=2, pady=10)

        self.editButton = ctk.CTkButton(self, text="Confirm Edit",
                            command=self.submit_item)
        self.editButton.grid(row=5, column=3, columnspan=2)

        self.listbox = tk.Listbox(self, width=60)
        self.listbox.grid(row=0, column=1, columnspan=4, rowspan=5, sticky='w', padx=20)

        self.listbox.bind("<<ListboxSelect>>", self.edit)

        self.collectMenu = ctk.CTkButton(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.collectMenu.grid(row=6, column=0)

        self.registerMenu = ctk.CTkButton(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.registerMenu.grid(row=6, column=1) #button4

        self.editMenu = ctk.CTkButton(self, text="Editar", state='disabled')
        self.editMenu.grid(row=6, column=2) #button5

        self.deleteMenu = ctk.CTkButton(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.deleteMenu.grid(row=6, column=3) #button6

        self.addUserMenu = ctk.CTkButton(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.addUserMenu.grid(row=6, column=4) #button7

        self.settingsMenu = ctk.CTkButton(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.settingsMenu.grid(row=6, column=5) #button8


class AdminDelete(ctk.CTkFrame):

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
        self.nome = self.listbox.get("anchor")

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
        ctk.CTkFrame.__init__(self, parent)

        # 'Nome' entry
        self.nameEntry = ctk.CTkEntry(self) 
        self.nameEntry.insert(0, "Nome")
        self.nameEntry.grid(row=0, column=0, columnspan=5, sticky='w')

        # 'ID' entry
        self.idEntry = ctk.CTkEntry(self) 
        self.idEntry.insert(0, "ID")
        self.idEntry.grid(row=1, column=0, columnspan=5, sticky='w')

        # 'Dosagem' entry
        self.doseEntry = ctk.CTkEntry(self) 
        self.doseEntry.insert(0, "Dosagem")
        self.doseEntry.grid(row=2, column=0, columnspan=5, sticky='w')

        # 'Apresentação' entry
        self.presentationEntry = ctk.CTkEntry(self) 
        self.presentationEntry.insert(0, "Apresentação")
        self.presentationEntry.grid(row=3, column=0, columnspan=5, sticky='w')

        # 'Position' entry
        self.positionEntry = ctk.CTkEntry(self) 
        self.positionEntry.insert(0, "Posição")
        self.positionEntry.grid(row=4, column=0, columnspan=5, sticky='w')

        self.searchButton = ctk.CTkButton(self, text="Pesquisar",
                            command=self.update_listbox)
        self.searchButton.grid(row=5, column=1, columnspan=2, pady=10)

        self.deleteButton = ctk.CTkButton(self, text="Confirm Delete",
                            command=self.delete)
        self.deleteButton.grid(row=5, column=3, columnspan=2)

        self.listbox = tk.Listbox(self, width=60)
        self.listbox.grid(row=0, column=1, columnspan=4, rowspan=5, sticky='w', padx=20)

        #self.listbox.bind("<<ListboxSelect>>", self.edit)

        self.collectMenu = ctk.CTkButton(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.collectMenu.grid(row=6, column=0)

        self.registerMenu = ctk.CTkButton(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.registerMenu.grid(row=6, column=1) #button4

        self.editMenu = ctk.CTkButton(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.editMenu.grid(row=6, column=2) #button5

        self.deleteMenu = ctk.CTkButton(self, text="Apagar", state='disabled')
        self.deleteMenu.grid(row=6, column=3) #button6

        self.addUserMenu = ctk.CTkButton(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.addUserMenu.grid(row=6, column=4) #button7

        self.settingsMenu = ctk.CTkButton(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.settingsMenu.grid(row=6, column=5) #button8

class AddUser(ctk.CTkFrame):

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
        ctk.CTkFrame.__init__(self, parent)

        self.nameLabel = ctk.CTkLabel(self, text="Nome", font=LARGE_FONT)
        self.nameLabel.grid(row=0, column=2, columnspan=2, sticky='w')

        self.nameEntry = ctk.CTkEntry(self) 
        self.nameEntry.grid(row=1, column=2, columnspan=2, sticky='nsew')

        self.nuspLabel = ctk.CTkLabel(self, text="NUSP", font=LARGE_FONT)
        self.nuspLabel.grid(row=2, column=2, columnspan=2, sticky='w')

        self.nuspEntry = ctk.CTkEntry(self) 
        self.nuspEntry.grid(row=3, column=2, columnspan=2, sticky='nsew')

        self.rfidLabel = ctk.CTkLabel(self, text="Card ID (RFID)", font=LARGE_FONT)
        self.rfidLabel.grid(row=4, column=2, columnspan=2, sticky='w')

        self.rfidEntry = ctk.CTkEntry(self) 
        self.rfidEntry.grid(row=5, column=2, columnspan=2, sticky='nsew')

        self.passwordLabel = ctk.CTkLabel(self, text="Senha", font=LARGE_FONT)
        self.passwordLabel.grid(row=6, column=2, columnspan=2, sticky='w')

        self.passwordEntry = ctk.CTkEntry(self, show='*') 
        self.passwordEntry.grid(row=7, column=2, columnspan=2, sticky='nsew')
        
        self.confirmpasswordLabel = ctk.CTkLabel(self, text="Confirmar Senha", font=LARGE_FONT)
        self.confirmpasswordLabel.grid(row=8, column=2, columnspan=2, sticky='w')

        self.confirmpasswordEntry = ctk.CTkEntry(self, show='*') 
        self.confirmpasswordEntry.grid(row=9, column=2, columnspan=2, sticky='nsew')

        self.isAdm = tk.IntVar()
        self.admBox = ctk.CTkCheckBox(self, text = "Administrador(a)", variable=self.isAdm)
        self.admBox.grid(row=10, column=2, sticky='w', pady=10, padx=5)

        self.addButton = ctk.CTkButton(self, text="Adicionar",
                            command=self.submit_user)
        self.addButton.grid(row=10, column=3)

        self.collectMenu = ctk.CTkButton(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.collectMenu.grid(row=11, column=0, pady=20)

        self.registerMenu = ctk.CTkButton(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.registerMenu.grid(row=11, column=1) #button4

        self.editMenu = ctk.CTkButton(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.editMenu.grid(row=11, column=2) #button5

        self.deleteMenu = ctk.CTkButton(self, text="Apagar", state='disabled')
        self.deleteMenu.grid(row=11, column=3) #button6

        self.addUserMenu = ctk.CTkButton(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.addUserMenu.grid(row=11, column=4) #button7

        self.settingsMenu = ctk.CTkButton(self, text="Configurações",
                        command=lambda: controller.show_frame(AdminConfig))
        self.settingsMenu.grid(row=11, column=5) #button8

class AdminConfig(ctk.CTkFrame):

    def logout(self, controller):
        controller.frames[StartPage].userEntry.delete(0, 'end')
        controller.frames[StartPage].passwordEntry.delete(0, 'end')
        controller.show_frame(StartPage)

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        # 'Log-in' button 
        self.logoutButton = ctk.CTkButton(self, text='Log-out', command=lambda: self.logout(controller))
        self.logoutButton.grid(row=0, column=2, columnspan=2)

        self.collectMenu = ctk.CTkButton(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.collectMenu.grid(row=6, column=0, pady=20)

        self.registerMenu = ctk.CTkButton(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.registerMenu.grid(row=6, column=1) #button4

        self.editMenu = ctk.CTkButton(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.editMenu.grid(row=6, column=2) #button5

        self.deleteMenu = ctk.CTkButton(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.deleteMenu.grid(row=6, column=3) #button6

        self.addUserMenu = ctk.CTkButton(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.addUserMenu.grid(row=6, column=4) #button7

        self.settingsMenu = ctk.CTkButton(self, text="Configurações", state='disabled')
        self.settingsMenu.grid(row=6, column=5) #button8


if __name__ == "__main__":
    from golgi_main import GolgiApp
    app = GolgiApp()
    app.mainloop()