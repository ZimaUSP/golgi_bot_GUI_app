import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from data_users import golgi_users
from dataframe import *
from math import ceil
from queue import Queue
from request import list_to_queue, communication

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
        # if adm:
        #     controller.show_frame(Register)
        # else:
        #     controller.show_frame(Register)

    return

class StartPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        # 'Usuário' label
        self.label1 = ctk.CTkLabel(self, text='Usuário: ', font=FONT)
        self.label1.pack()

        # 'Usuário' entry
        self.entry1 = ctk.CTkEntry(self, font=FONT) 
        self.entry1.pack()
        self.entry1.delete(0)

        # Empty label, skip line
        self.emptyLabel = ctk.CTkLabel(self, text=' ')
        self.emptyLabel.pack()

        # 'Senha' label
        self.label2 = ctk.CTkLabel(self, text='Senha: ', font=FONT)
        self.label2.pack()

        # 'Senha' entry
        self.entry2 = ctk.CTkEntry(self, show="*", font=FONT) 
        self.entry2.pack()

        self.entry2.bind('<Return>', (lambda func : login(self.entry1.get(), self.entry2.get(), controller)))

        # Empty label, skip line
        self.emptyLabel = ctk.CTkLabel(self, text=' ')
        self.emptyLabel.pack()

        # 'Entrar' button 
        self.button2 = ctk.CTkButton(self, text='Entrar', font=FONT, command=lambda: login(self.entry1.get(), self.entry2.get(), controller))
        self.button2.pack(pady=10)

        # 'Esqueci minha senha' button
        self.button1 = ctk.CTkButton(self, text='Esqueci minha senha', font=FONT, command= lambda: reset_password(controller))
        self.button1.pack()


class ResetPassword(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.label = ctk.CTkLabel(self, text="Esqueci minha senha", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        self.label1 = ctk.CTkLabel(self, text="Por favor, entre em contato com a organização\npor meio do número: (99) 99999-9999", font=FONT)
        self.label1.pack(pady=20)

        self.button1 = ctk.CTkButton(self, text="Retornar ao menu principal", font=FONT,
                            command=lambda: controller.show_frame(StartPage))
        self.button1.pack(pady=20)

class AdminCollect1(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        


        self.label1 = tk.Label(self, text="Paciente", font=LARGE_FONT)
        self.label1.grid(row=0, column=0, columnspan=3, sticky='w')

        self.entry1 = tk.Entry(self) 
        self.entry1.grid(row=1, column=0, columnspan=3, sticky='w')

        self.label2 = tk.Label(self, text="ID", font=LARGE_FONT)
        self.label2.grid(row=2, column=0, columnspan=3, sticky='w')

        self.entry2 = tk.Entry(self) 
        self.entry2.grid(row=3, column=0, columnspan=3, sticky='w')

        self.button1 = ttk.Button(self, text="Submit",
                            command=lambda: controller.show_frame(AdminCollect2))
        self.button1.grid(row=4, column=0, columnspan=3)

        self.button3 = ttk.Button(self, text="Coletar", state='disabled')
        self.button3.grid(row=5, column=0)

        self.button4 = ttk.Button(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button4.grid(row=5, column=1)

        self.button5 = ttk.Button(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.button5.grid(row=5, column=2)

        self.button6 = ttk.Button(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.button6.grid(row=5, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=5, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.button8.grid(row=5, column=5)


class AdminCollect2(ctk.CTkFrame):

    def display(self, event):
        self.entry2.delete(0, "end")
        self.entry1.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")
        #self.entry5.delete(0, "end")

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
        #self.position = self.data.position[0]

        #print(self.id, self.nome, self.dose, self.apresentacao, self.position)

        self.entry2.insert(0, str(self.id))
        self.entry1.insert(0, str(self.nome))
        self.entry3.insert(0, str(self.dose))
        self.entry4.insert(0, str(self.apresentacao))
        #self.entry5.insert(0, str(self.position))

        
        if self.id in self.collect_list.keys():
            self.lbl_value["text"] = str(int(self.collect_list[self.id]))

        else:
            self.lbl_value["text"] = "0"

        

    # update listbox
    def update_listbox(self):
        self.listbox.delete(0, "end")

        self.id = self.entry2.get()
        self.nome = self.entry1.get()
        self.dose = self.entry3.get()
        self.apresentacao = self.entry4.get()

        if self.id == "ID":
            self.id = ""

        if self.nome == "Nome":
            self.nome = ""

        if self.dose == "Dose":
            self.dose = ""

        if self.apresentacao == "Apresentação":
            self.apresentacao = ""

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)

        # for item in self.data.nome:
        #     self.listbox.insert("end", item)

        for i in range(len(self.data.nome)-1):
            self.listbox.insert("end", self.data.nome[i])

    def increase(self):
        value = int(self.lbl_value["text"])
        self.lbl_value["text"] = f"{value + 1}"

    def decrease(self):
        value = int(self.lbl_value["text"])
        if value > 0:
            self.lbl_value["text"] = f"{value - 1}"

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
        queue = list_to_queue(self.collect_list)
        communication(queue)

        return True
        

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        

        self.collect_list = {}

        #self.collect_list = Queue(maxsize = 0)

        # 'Nome' entry
        self.entry1 = tk.Entry(self) 
        self.entry1.insert(0, "Nome")
        self.entry1.grid(row=0, column=0, columnspan=5, sticky='w')

        # 'ID' entry
        self.entry2 = tk.Entry(self) 
        self.entry2.insert(0, "ID")
        self.entry2.grid(row=1, column=0, columnspan=5, sticky='w')

        # 'Dosagem' entry
        self.entry3 = tk.Entry(self) 
        self.entry3.insert(0, "Dosagem")
        self.entry3.grid(row=2, column=0, columnspan=5, sticky='w')

        # 'Apresentação' entry
        self.entry4 = tk.Entry(self) 
        self.entry4.insert(0, "Apresentação")
        self.entry4.grid(row=3, column=0, columnspan=5, sticky='w')

        self.button1 = ttk.Button(self, text="Pesquisar",
                            command=self.update_listbox)
        self.button1.grid(row=5, column=1, columnspan=1)

        self.button2 = ttk.Button(self, text="Coletar", command=self.collect)
        self.button2.grid(row=5, column=2, columnspan=1)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.grid(row=0, column=1, columnspan=4, rowspan=4)

        self.listbox.bind("<<ListboxSelect>>", self.display)

        self.btn_decrease = ttk.Button(master=self, text="-", command=self.decrease)
        self.btn_decrease.grid(row=2, column=5)

        self.lbl_value = ttk.Label(master=self, text="0")
        self.lbl_value.grid(row=2, column=6)

        self.btn_increase = ttk.Button(master=self, text="+", command=self.increase)
        self.btn_increase.grid(row=2, column=7)

        self.add_button = ttk.Button(self, text="Adicionar", command=self.add_to_queue)
        self.add_button.grid(row=3, column=5)

        self.button3 = ttk.Button(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.button3.grid(row=6, column=0)

        self.button4 = ttk.Button(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button4.grid(row=6, column=1)

        self.button5 = ttk.Button(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.button5.grid(row=6, column=2)

        self.button6 = ttk.Button(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.button6.grid(row=6, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=6, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.button8.grid(row=6, column=5)


class AdminRegister(ctk.CTkFrame):

    def submit_item(self):
        """Callback function to register new item in dataset

        Returns:
            bool: True if all fields were completed
        """
        self.id = self.entry2.get()
        self.nome = self.entry1.get()
        self.dose = self.entry3.get()
        self.apresentacao = self.entry4.get()
        self.position = self.entry5.get()
    
        

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
            golgi_data.add_item(item)
            golgi_data.save_to_disk()

            self.entry2.delete(0, "end")
            self.entry1.delete(0, "end")
            self.entry3.delete(0, "end")
            self.entry4.delete(0, "end")
            self.entry5.delete(0, "end")

            self.entry2.insert(0, "ID")
            self.entry1.insert(0, "Nome")
            self.entry3.insert(0, "Dosagem")
            self.entry4.insert(0, "Apresentação")
            self.entry5.insert(0, "Posição")

            return True

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        

        # 'Nome' entry
        self.entry1 = tk.Entry(self) 
        self.entry1.insert(0, "Nome")
        self.entry1.grid(row=0, column=0, columnspan=5, sticky='w')

        # 'ID' entry
        self.entry2 = tk.Entry(self) 
        self.entry2.insert(0, "ID")
        self.entry2.grid(row=1, column=0, columnspan=5, sticky='w')

        # 'Dosagem' entry
        self.entry3 = tk.Entry(self) 
        self.entry3.insert(0, "Dosagem")
        self.entry3.grid(row=2, column=0, columnspan=5, sticky='w')

        # 'Apresentação' entry
        self.entry4 = tk.Entry(self) 
        self.entry4.insert(0, "Apresentação")
        self.entry4.grid(row=3, column=0, columnspan=5, sticky='w')

        # 'Position' entry
        self.entry5 = tk.Entry(self) 
        self.entry5.insert(0, "Posição")
        self.entry5.grid(row=4, column=0, columnspan=5, sticky='w')

        self.button1 = ttk.Button(self, text="Registrar",
                            command=lambda: self.submit_item())
        self.button1.grid(row=5, column=0, columnspan=3)

        self.button3 = ttk.Button(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.button3.grid(row=6, column=0)

        self.button4 = ttk.Button(self, text="Registrar", state='disabled')
        self.button4.grid(row=6, column=1)

        self.button5 = ttk.Button(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.button5.grid(row=6, column=2)

        self.button6 = ttk.Button(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.button6.grid(row=6, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=6, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.button8.grid(row=6, column=5)
        

class AdminEdit(ctk.CTkFrame):

    def edit(self, event):
        self.entry2.delete(0, "end")
        self.entry1.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")
        self.entry5.delete(0, "end")

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

        self.entry2.insert(0, str(self.id))
        self.entry1.insert(0, str(self.nome))
        self.entry3.insert(0, str(self.dose))
        self.entry4.insert(0, str(self.apresentacao))
        self.entry5.insert(0, str(self.position))


    # update listbox
    def update_listbox(self):
        self.listbox.delete(0, "end")

        self.id = self.entry2.get()
        self.nome = self.entry1.get()
        self.dose = self.entry3.get()
        self.apresentacao = self.entry4.get()
        self.posicao = self.entry5.get()

        if self.id == "ID":
            self.id = ""

        if self.nome == "Nome":
            self.nome = ""

        if self.dose == "Dose":
            self.dose = ""

        if self.apresentacao == "Apresentação":
            self.apresentacao = ""

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)

        # for item in self.data.nome:
        #     self.listbox.insert("end", item)

        for i in range(len(self.data.nome)-1):
            self.listbox.insert("end", self.data.nome[i])



    def submit_item(self):
        """Callback function to register edited item

        Returns:
            bool: True if all fields are completed
        """
        self.id = self.entry2.get()
        self.nome = self.entry1.get()
        self.dose = self.entry3.get()
        self.apresentacao = self.entry4.get()
        self.position = self.entry5.get()

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
            self.entry2.delete(0, "end")
            self.entry1.delete(0, "end")
            self.entry3.delete(0, "end")
            self.entry4.delete(0, "end")
            self.entry5.delete(0, "end")

            self.entry2.insert(0, "ID")
            self.entry1.insert(0, "Nome")
            self.entry3.insert(0, "Dosagem")
            self.entry4.insert(0, "Apresentação")
            self.entry5.insert(0, "Posição")


            return True


    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        

        # 'Nome' entry
        self.entry1 = tk.Entry(self) 
        self.entry1.insert(0, "Nome")
        self.entry1.grid(row=0, column=0, columnspan=4, sticky='w')

        # 'ID' entry
        self.entry2 = tk.Entry(self) 
        self.entry2.insert(0, "ID")
        self.entry2.grid(row=1, column=0, columnspan=4, sticky='w')

        # 'Dosagem' entry
        self.entry3 = tk.Entry(self) 
        self.entry3.insert(0, "Dosagem")
        self.entry3.grid(row=2, column=0, columnspan=4, sticky='w')

        # 'Apresentação' entry
        self.entry4 = tk.Entry(self) 
        self.entry4.insert(0, "Apresentação")
        self.entry4.grid(row=3, column=0, columnspan=4, sticky='w')

        # 'Position' entry
        self.entry5 = tk.Entry(self) 
        self.entry5.insert(0, "Posição")
        self.entry5.grid(row=4, column=0, columnspan=4, sticky='w')

        self.button1 = ttk.Button(self, text="Submit",
                            command=self.update_listbox)
        self.button1.grid(row=5, column=0, columnspan=3)

        self.button2 = ttk.Button(self, text="Confirm Edit",
                            command=self.submit_item)
        self.button2.grid(row=5, column=1, columnspan=3)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.grid(row=0, column=2, columnspan=4, rowspan=5)

        self.listbox.bind("<<ListboxSelect>>", self.edit)

        self.button3 = ttk.Button(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.button3.grid(row=6, column=0)

        self.button4 = ttk.Button(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button4.grid(row=6, column=1)

        self.button5 = ttk.Button(self, text="Editar", state='disabled')
        self.button5.grid(row=6, column=2)

        self.button6 = ttk.Button(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.button6.grid(row=6, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=6, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.button8.grid(row=6, column=5)


class AdminDelete(ctk.CTkFrame):

    def edit(self, event):
        self.entry2.delete(0, "end")
        self.entry1.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")
        self.entry5.delete(0, "end")

        self.id = ""
        self.dose = ""
        self.apresentacao = ""
        self.nome = self.listbox.get("anchor")
        #self.nome = self.listbox.get(self.listbox.curselection())
        
        print(self.nome)

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)
        self.data = self.data.reset_index()

        self.id = self.data.id[0]
        self.nome = self.data.nome[0]
        self.dose = self.data.dosagem[0]
        self.apresentacao = self.data.apresentacao[0]
        self.position = self.data.position[0]

        print(self.nome)
        self.entry2.insert(0, str(self.id))
        self.entry1.insert(0, str(self.nome))
        self.entry3.insert(0, str(self.dose))
        self.entry4.insert(0, str(self.apresentacao))
        self.entry5.insert(0, str(self.position))


    # update listbox
    def update_listbox(self):
        self.listbox.delete(0, "end")

        self.id = self.entry2.get()
        self.nome = self.entry1.get()
        self.dose = self.entry3.get()
        self.apresentacao = self.entry4.get()
        self.posicao = self.entry5.get()

        if self.id == "ID":
            self.id = ""

        if self.nome == "Nome":
            self.nome = ""

        if self.dose == "Dose":
            self.dose = ""

        if self.apresentacao == "Apresentação":
            self.apresentacao = ""

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)

        # for item in self.data.nome:
        #     self.listbox.insert("end", item)

        for i in range(len(self.data.nome)-1):
            self.listbox.insert("end", self.data.nome[i])



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

        self.entry2.delete(0, "end")
        self.entry1.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")
        self.entry5.delete(0, "end")

        self.entry2.insert(0, "ID")
        self.entry1.insert(0, "Nome")
        self.entry3.insert(0, "Dosagem")
        self.entry4.insert(0, "Apresentação")
        self.entry5.insert(0, "Posição")


    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        

        # 'Nome' entry
        self.entry1 = tk.Entry(self) 
        self.entry1.insert(0, "Nome")
        self.entry1.grid(row=0, column=0, columnspan=4, sticky='w')

        # 'ID' entry
        self.entry2 = tk.Entry(self) 
        self.entry2.insert(0, "ID")
        self.entry2.grid(row=1, column=0, columnspan=4, sticky='w')

        # 'Dosagem' entry
        self.entry3 = tk.Entry(self) 
        self.entry3.insert(0, "Dosagem")
        self.entry3.grid(row=2, column=0, columnspan=4, sticky='w')

        # 'Apresentação' entry
        self.entry4 = tk.Entry(self) 
        self.entry4.insert(0, "Apresentação")
        self.entry4.grid(row=3, column=0, columnspan=4, sticky='w')

        # 'Position' entry
        self.entry5 = tk.Entry(self) 
        self.entry5.insert(0, "Posição")
        self.entry5.grid(row=4, column=0, columnspan=4, sticky='w')

        self.button1 = ttk.Button(self, text="Submit",
                            command=self.update_listbox)
        self.button1.grid(row=5, column=0, columnspan=3)

        self.button2 = ttk.Button(self, text="Confirm Delete",
                            command=self.delete)
        self.button2.grid(row=5, column=1, columnspan=3)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.grid(row=0, column=2, columnspan=4, rowspan=5)

        #self.listbox.bind("<<ListboxSelect>>", self.edit)

        self.button3 = ttk.Button(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.button3.grid(row=6, column=0)

        self.button4 = ttk.Button(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button4.grid(row=6, column=1)

        self.button5 = ttk.Button(self, text="Editar", 
                            command=lambda: controller.show_frame(AdminEdit))
        self.button5.grid(row=6, column=2)

        self.button6 = ttk.Button(self, text="Apagar",state='disabled')
        self.button6.grid(row=6, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=6, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.button8.grid(row=6, column=5)

class AddUser(ctk.CTkFrame):

    def submit_user(self):
        """Callback function to register new user in dataset

        Returns:
            bool: True if all fields were completed
        """
        self.nome = self.entry1.get()
        self.nusp = self.entry2.get()
        self.rfid = self.entry3.get()
        self.senha = self.entry4.get()
        self.senha_verify = self.entry5.get()
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

        

        # 'Nome' entry
        self.entry1 = ttk.Entry(self) 
        self.entry1.insert(0, "Nome")
        self.entry1.grid(row=0, column=0, sticky='w')

        # 'NUSP' entry
        self.entry2 = ttk.Entry(self) 
        self.entry2.insert(0, "ID")
        self.entry2.grid(row=0, column=1, sticky='w')

        # 'Card ID (RFID)' entry
        self.entry3 = ttk.Entry(self) 
        self.entry3.insert(0, "Card ID (RFID)")
        self.entry3.grid(row=1, column=0,  sticky='w')

        # 'Senha' entry
        self.entry4 = ttk.Entry(self) 
        self.entry4.insert(0, "Senha")
        self.entry4.grid(row=1, column=1, sticky='w')

        # 'Confirmar senha' entry
        self.entry5 = ttk.Entry(self) 
        self.entry5.insert(0, "Confirmar senha")
        self.entry5.grid(row=2, column=0, sticky='w')

        self.isAdm = tk.IntVar()
        self.admBox = ttk.Checkbutton(self, text = "Administrador(a)", variable=self.isAdm)
        self.admBox.grid(row=2, column=1, sticky='w')

        self.button1 = ttk.Button(self, text="Adicionar",
                            command=self.submit_user)
        self.button1.grid(row=3, column=0)

        self.button3 = ttk.Button(self, text="Coletar",
                            command=lambda: controller.show_frame(AdminCollect1))
        self.button3.grid(row=5, column=0)

        self.button4 = ttk.Button(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button4.grid(row=5, column=1)

        self.button5 = ttk.Button(self, text="Editar",
                            command=lambda: controller.show_frame(AdminEdit))
        self.button5.grid(row=5, column=2)

        self.button6 = ttk.Button(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminDelete))
        self.button6.grid(row=5, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário", state='disabled')
        self.button7.grid(row=5, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminConfig))
        self.button8.grid(row=5, column=5)

class AdminConfig(ctk.CTkFrame):

    def logout(self, controller):
        controller.frames[StartPage].entry1.delete(0, 'end')
        controller.frames[StartPage].entry2.delete(0, 'end')
        controller.show_frame(StartPage)

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        

        # 'Log-in' button 
        self.button = ttk.Button(self, text='Log-out', command=lambda: self.logout(controller))
        self.button.grid(row=1, column=2, columnspan=2)

        self.button3 = ttk.Button(self, text="Coletar", 
                            command=lambda: controller.show_frame(AdminCollect1))
        self.button3.grid(row=2, column=0)

        self.button4 = ttk.Button(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button4.grid(row=2, column=1)

        self.button5 = ttk.Button(self, text="Editar", 
                            command=lambda: controller.show_frame(AdminEdit))
        self.button5.grid(row=2, column=2)

        self.button6 = ttk.Button(self, text="Apagar", 
                            command=lambda: controller.show_frame(AdminDelete))
        self.button6.grid(row=2, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=2, column=4)

        self.button8 = ttk.Button(self, text="Configurações", state='disabled')
        self.button8.grid(row=2, column=5)


if __name__ == "__main__":
    from golgi_main import GolgiApp
    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
    app = GolgiApp()
    app.mainloop()