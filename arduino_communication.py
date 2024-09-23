from CTkMessagebox.CTkMessagebox import *
from tkinter import messagebox
from serial import Serial
import time

class ArduinoCommunication():
    def __init__(self):
        #self.parent = app # guarda referência ao programa principal
        self.baudrate = 9600 # define o baudrate padrao

    def connect(self, port):
        try:
            print("ESP se conectando na porta", port)
            self.ser = Serial(port, self.baudrate) # tenta conectar ao Arduino
            #self.parent.connected = True # indica que está conectado
            #self.parent.COM_port = port # guarda a porta COM
            return True
        
        except Exception as e:
            print(e)
            print("A conexão falhou!") # se não conseguir conectar, mostra mensagem de erro
            return False

    def send_message(self, message):
        self.ser.write(message) 
        print(message)
        serial_out = self.ser.readline().decode().strip()
        while(serial_out != "STAND-BY"):
            serial_out = self.ser.readline().decode().strip()
            print(serial_out)
        print(serial_out)
        
