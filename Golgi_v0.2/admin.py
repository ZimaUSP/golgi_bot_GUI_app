import tkinter as tk
from tkinter import ttk
from data_users import golgi_users
from dataframe import *
from math import ceil



LARGE_FONT= ("Verdana", 12)

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

class StartPage(tk.Frame): #Done

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.configure(bg='#303030')

        # 'Usuário' label
        self.label1 = tk.Label(self, text='Usuário: ')
        self.label1.config(font=('helvetica', 14), bg='#303030', fg='#999999')
        self.label1.grid(row=0, column=0, sticky='w')

        # 'Usuário' entry
        self.entry1 = tk.Entry(self) 
        self.entry1.grid(row=1, column=0, columnspan=3, sticky='w')

        # Empty label, skip line
        self.emptyLabel = tk.Label(self, text=' ', bg='#303030')
        self.emptyLabel.grid(row=2, column=0)

        # 'Senha' label
        self.label2 = tk.Label(self, text='Senha: ')
        self.label2.config(font=('helvetica', 14), bg='#303030', fg='#999999')
        self.label2.grid(row=3, column=0, sticky='w')

        # 'Senha' entry
        self.entry2 = tk.Entry(self, show="*") 
        self.entry2.grid(row=4, column=0,columnspan=3, sticky='w')

        self.entry2.bind('<Return>', (lambda func : login(self.entry1.get(), self.entry2.get(), controller)))

        # 'Esqueci minha senha' button
        self.button1 = ttk.Button(self, text='Esqueci minha senha', command= lambda: reset_password(controller))
        self.button1.grid(row=5, column=3)

        # 'Entrar' button 
        self.button2 = ttk.Button(self, text='Entrar', command=lambda: login(self.entry1.get(), self.entry2.get(), controller))
        self.button2.grid(row=6, column=0, columnspan=3)

        # 'Ajuda' button 
        self.button3 = ttk.Button(self, text='Ajuda', command= lambda: help(controller))
        self.button3.grid(row=7, column=1, columnspan=3)

        


class ResetPassword(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='#303030')

        self.label = tk.Label(self, text="Esqueci a Senha!!!", font=LARGE_FONT)
        self.label.pack(pady=10,padx=10)

        self.button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        self.button1.pack()

        self.button2 = ttk.Button(self, text="ENTRAR",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button2.pack()

class AdminCollect1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='#303030')


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
                            command=lambda: controller.show_frame(AdminRegister))
        self.button6.grid(row=5, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=5, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button8.grid(row=5, column=5)


class AdminCollect2(tk.Frame):

    def on_submit(self):
        """Callback function to search itens from Pandas dataset
        """

        self.id = self.entry2.get()
        self.nome = self.entry1.get()
        self.dose = self.entry3.get()
        self.apresentacao = self.entry4.get()

        self.data = golgi_data.get_items(id = self.id, nome = self.nome, dosagem=self.dose, apresentacao=self.apresentacao)
        #self.ids.resultados.ids.main_layout_resultados.clear_widgets()
        self.entry2.delete(0, "end")
        self.entry1.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")

        self.entry2.insert(0, "ID")
        self.entry1.insert(0, "Nome")
        self.entry3.insert(0, "Dosagem")
        self.entry4.insert(0, "Apresentação")

        self.data = self.data.reset_index()
        self.n_items  = len(self.data.index)
        self.n_pages = ceil(self.n_items/15.0)
        
        print(self.n_items)

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

        for item in self.data.nome:
            self.listbox.insert("end", item)
        

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='#303030')

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

        self.button1 = ttk.Button(self, text="Submit",
                            command=self.update_listbox)
        self.button1.grid(row=5, column=0, columnspan=3)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.grid(row=0, column=1, columnspan=4, rowspan=4)

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
                            command=lambda: controller.show_frame(AdminRegister))
        self.button6.grid(row=6, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=6, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button8.grid(row=6, column=5)


class AdminRegister(tk.Frame):

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
        tk.Frame.__init__(self, parent)

        self.configure(bg='#303030')

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
                            command=lambda: controller.show_frame(AdminRegister))
        self.button6.grid(row=6, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=6, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button8.grid(row=6, column=5)
        

class AdminEdit(tk.Frame):

    def edit(self, event):
        self.entry2.delete(0, "end")
        self.entry1.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")
        #self.entry5.delete(0, "end")

        # self.id = ""
        # self.dose = ""
        # self.apresentacao = ""
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
        #self.entry5.insert(0, str(self.position))


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

        for item in self.data.nome:
            self.listbox.insert("end", item)



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


        new_path = ""

        if (self.nome == "" or self.id == "" or self.dose == "" or self.apresentacao == "" or self.position == ""):
            print("Complete form!\n")
            print(self.nome + "\n")
            print(self.id + "\n")
            print(self.position + "\n")
            print(self.dose + "\n")
            print(self.apresentacao + "\n")
            return False
        else:
            #golgi_data.delete_item(int(float(self.id)))
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
        tk.Frame.__init__(self, parent)

        self.configure(bg='#303030')

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

        self.button1 = ttk.Button(self, text="Submit",
                            command=self.update_listbox)
        self.button1.grid(row=5, column=0, columnspan=3)

        self.button2 = ttk.Button(self, text="Confirm Edit",
                            command=self.submit_item)
        self.button2.grid(row=5, column=1, columnspan=3)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.grid(row=0, column=1, columnspan=4, rowspan=4)

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
                            command=lambda: controller.show_frame(AdminRegister))
        self.button6.grid(row=6, column=3)

        self.button7 = ttk.Button(self, text="Adicionar Usuário",
                        command=lambda: controller.show_frame(AddUser))
        self.button7.grid(row=6, column=4)

        self.button8 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminRegister))
        self.button8.grid(row=6, column=5)


class Help(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='#303030')


        self.label = tk.Label(self, text="Texto Página de Ajuda", font=LARGE_FONT)
        self.label.grid(row=0, column=0, columnspan=3)

        # 'Log-in' button 
        self.button = ttk.Button(self, text='Log-in', command=lambda: controller.show_frame(StartPage))
        self.button.grid(row=1, column=0, columnspan=3)

        # 'Ajuda' button 
        self.button2 = ttk.Button(self, text='Ajuda', state='disabled')
        self.button2.grid(row=1, column=2, columnspan=3)


class AddUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='#303030')

        # 'Nome' entry
        entry1 = tk.Entry(self) 
        entry1.insert(0, "Nome")
        entry1.grid(row=0, column=0, sticky='w')

        # 'NUSP' entry
        entry2 = tk.Entry(self) 
        entry2.insert(0, "ID")
        entry2.grid(row=0, column=1, sticky='w')

        # 'Card ID (RFID)' entry
        entry3 = tk.Entry(self) 
        entry3.insert(0, "Card ID (RFID)")
        entry3.grid(row=1, column=0,  sticky='w')

        # 'Senha' entry
        entry4 = tk.Entry(self) 
        entry4.insert(0, "Senha")
        entry4.grid(row=1, column=1, sticky='w')

        # 'Confirmar senha' entry
        entry4 = tk.Entry(self) 
        entry4.insert(0, "Confirmar senha")
        entry4.grid(row=2, column=0, sticky='w')

        admBox = tk.Checkbutton(self, text = "Administrador(a)")
        admBox.grid(row=2, column=1, sticky='w')

        button3 = ttk.Button(self, text="Coletar",
                            command=lambda: controller.show_frame(AdminRegister))
        button3.grid(row=5, column=0)

        button4 = ttk.Button(self, text="Registrar",
                            command=lambda: controller.show_frame(AdminRegister))
        button4.grid(row=5, column=1)

        button5 = ttk.Button(self, text="Editar",
                            command=lambda: controller.show_frame(AdminRegister))
        button5.grid(row=5, column=2)

        button6 = ttk.Button(self, text="Apagar",
                            command=lambda: controller.show_frame(AdminRegister))
        button6.grid(row=5, column=3)

        button6 = ttk.Button(self, text="Adicionar Usuário",
                            command=lambda: controller.show_frame(AdminRegister))
        button6.grid(row=5, column=4)

        button7 = ttk.Button(self, text="Configurações",
                            command=lambda: controller.show_frame(AdminRegister))
        button7.grid(row=5, column=5)