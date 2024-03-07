from tkinter import *

# Define button functions
def reset_password():
    return

def login():
    #add popup if wrong password
    return

# Create and configure main window
root = Tk()

root.iconbitmap("Golgi_v0.2/images/logo-gradient.ico")

root.title('Golgi v0.2')

root.geometry("600x600")

root.configure(bg='#303030')

# 'Usuário' label
label1 = Label(root, text='Usuário: ')
label1.config(font=('helvetica', 14), bg='#303030', fg='#999999')
label1.grid(row=0, column=0, sticky='w')

# 'Usuário' entry
entry1 = Entry(root) 
entry1.grid(row=1, column=0, columnspan=3, sticky='w')

# Empty label, skip line
emptyLabel = Label(root, text=' ', bg='#303030')
emptyLabel.grid(row=2, column=0)

# 'Senha' label
label2 = Label(root, text='Senha: ')
label2.config(font=('helvetica', 14), bg='#303030', fg='#999999')
label2.grid(row=3, column=0, sticky='w')

# 'Senha' entry
entry2 = Entry(root) 
entry2.grid(row=4, column=0,columnspan=3, sticky='w')

# 'Esqueci minha senha' button
button1 = Button(root, text='Esqueci minha senha', command=reset_password)
button1.grid(row=5, column=3)

# 'Entrar' button 
button2 = Button(root, text='Entrar', command=login)
button2.grid(row=6, column=0, columnspan=3)

root.mainloop()
