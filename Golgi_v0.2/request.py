"""
https://techtutorialsx.com/2017/12/02/esp32-esp8266-arduino-serial-communication-with-python/
"""

import serial
import time
try:
    from queue import Queue
except:
    import Queue

def communication():
    BAUDRATE = 115200
    PORT = '/dev/ttyUSB0'

    ser = serial.Serial()

    ser.baudrate = BAUDRATE
    ser.port = PORT
    ser.timeout = 0.1

    ser.open()

    values = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for i in values:
        print(i)
        ser.write(bytes(i))
        time.sleep(2)
        print(ser.readline())
    
    ser.close()

    return


def request(dict):
    q = Queue(maxsize = 0)

    items = dict.items()
    #print(dict)

    for key, value in items:
        for cont in range(value):
            q.put(key)

    print(q.queue)
    return
    
if __name__ == '__main__':
    #request({17297: 3, 21393: 2, 17312: 4, 19759: 8, 17342: 1})
    communication()
