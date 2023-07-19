"""
https://techtutorialsx.com/2017/12/02/esp32-esp8266-arduino-serial-communication-with-python/

https://www.hackster.io/ansh2919/serial-communication-between-python-and-arduino-e7cce0

"""

import serial
import time

from arduino_communication import ArduinoCommunication

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

def main():
    # list_to_queue({17297: 3, 21393: 2, 17312: 4, 19759: 8, 17342: 1})
    communication = ArduinoCommunication()
    connect = communication.connect('COM7')

    if connect:
        queue = ['0']
        for item in queue:
            item = bytes(item, encoding='utf-8')
            communication.send_message(item)
            time.sleep(2)
    
if __name__ == '__main__':
    main()



