import serial
import time

class ArduinoCommunication():
    def __init__(self):
        #self.parent = app # guarda referência ao programa principal
        self.baudrate = 9600 # define o baudrate padrao

    def connect(self, port):
        try:
            self.ser = serial.Serial(port, self.baudrate) # tenta conectar ao Arduino
            #self.parent.connected = True # indica que está conectado
            #self.parent.COM_port = port # guarda a porta COM
            print("ESP conectado na porta", port)
            return True
        
        except:
            print("A conexão falhou!") # se não conseguir conectar, mostra mensagem de erro
            return False

    def send_message(self, message):
        self.ser.write(message) 
        print(message)
        serial_out = self.ser.readline().decode()
        while(serial_out != "STAND-BY\r\n"):
            serial_out = self.ser.readline().decode()
            print(serial_out)
        
        