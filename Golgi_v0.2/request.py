"""
https://techtutorialsx.com/2017/12/02/esp32-esp8266-arduino-serial-communication-with-python/

https://www.hackster.io/ansh2919/serial-communication-between-python-and-arduino-e7cce0

"""

import serial
import time
try:
    from queue import Queue
except:
    import Queue

def communication1(values):
    print(values.queue)
    BAUDRATE = 9600
    PORT = 'COM7'

    ser = serial.Serial(baudrate=BAUDRATE, port=PORT,
                        timeout=0.1)
    
    ser.close()

    ser.open()
    
    for i in values.queue:
        print(repr(i))
        ser.write(bytes(str(int(2)), 'ascii'))
        seq = []
        joined_seq = ''

        while True:
            for c in ser.read():
                seq.append(chr(c)) #convert from ASCII
                joined_seq = ''.join(str(v) for v in seq) #Make a string from array

                if chr(c) == '\n':
                    print(joined_seq)
                    seq = []
                    break

            if joined_seq == 'STAND-BY':
                print(joined_seq)
                break

    print('Fim!')

        #time.sleep(1) # 1 segundos

    ser.close()

    return

def communication2(values):
    print(values.queue)
    BAUDRATE = 9600
    PORT = 'COM7'

    ser = serial.Serial(baudrate=BAUDRATE, port=PORT,
                        timeout=0.1)
    
    ser.close()

    ser.open()
    
    for i in values.queue:
        print(str(i))
        ser.write(bytes(str(int(i)), 'ascii'))
        
        while True:
            print(repr(ser.readline().decode()))
            if (repr(ser.readline().decode()) == 'STAND-BY\r\n'):
                break

    print("Fim!")

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
    q.put('2')
    q.put('3')

    #communication(q)
