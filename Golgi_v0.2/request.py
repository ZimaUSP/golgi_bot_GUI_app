"""
https://techtutorialsx.com/2017/12/02/esp32-esp8266-arduino-serial-communication-with-python/
"""

import serial
import time
try:
    from queue import Queue
except:
    import Queue

def communication(values):
    print(values.queue)
    BAUDRATE = 9600
    PORT = 'COM7'

    ser = serial.Serial()

    ser.baudrate = BAUDRATE
    ser.port = PORT
    ser.timeout = 0.1

    ser.open()
    
    for i in values.queue:
        print(i)
        #print(bytes(i))
        ser.write(bytes(str(i), 'ascii'))
        # ser.write(i)
        #ser.write(str(i).encode())
        #ser.write(bytearray([i]))
        time.sleep(10)
        ser.readline()
    
    ser.close()

    return


def list_to_queue(dict):
    q = Queue(maxsize = 0)

    items = dict.items()
    #print(dict)

    for key, value in items:
        for cont in range(value):
            q.put(key)

    print(q.queue)

    """
    Adicionar bloco que salva o dicionário recebido, com códigos pertinentes etc
    """
    return q
    
if __name__ == '__main__':
    #list_to_queue({17297: 3, 21393: 2, 17312: 4, 19759: 8, 17342: 1})
    q = Queue()
    q.put("2")
    communication(q)
