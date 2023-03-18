"""
https://techtutorialsx.com/2017/12/02/esp32-esp8266-arduino-serial-communication-with-python/

https://www.hackster.io/ansh2919/serial-communication-between-python-and-arduino-e7cce0

"""

import serial
import time
# try:
#     from queue import Queue
# except:
#     import Queue

def dict_to_list(dict):
    # q = Queue(maxsize = 0)
    q = []
    items = dict.items()
    #print(dict)

    for key, value in items:
        for cont in range(value):
            q.append(key)

    print(q)

    return q

def communication(queue):
    BAUDRATE = 9600
    PORT = 'COM3'

    ser = serial.Serial(baudrate=BAUDRATE, port=PORT,
                    timeout=0.1)

    string = ser.readline().decode() # TEM QUE SER READLINE, talvez tenha que alterar os prints do Golgi
    
    for command in queue:
        while string != "STAND-BY\r\n": # Aguarda o Golgi estar pronto
            string = ser.readline().decode() # TEM QUE SER READLINE, talvez tenha que alterar os prints do Golgi

            if string != "": 
                print(string)

        command += '\n' # Deve ser adaptado para o código do ESP 
        ser.write(command.encode('ascii')) # Escreve o comando (número) no serial

        string = "" # Lê os prints do Serial pelo Golgi

    string = ser.readline().decode() # TEM QUE SER READLINE, talvez tenha que alterar os prints do Golgi

    if string != "": 
        print(string)

    print("Fim!")

def main():
    # list_to_queue({17297: 3, 21393: 2, 17312: 4, 19759: 8, 17342: 1})
    queue = ['2']
    communication(queue)
    
if __name__ == '__main__':
    main()



