import serial
import struct
import threading
import time


def while_test(order):
    while expression:
        pass

thread_list = []
t1 = threading.Thread(target=while_test, args=("/dev/ttyUSB0",1,9))
t2 = threading.Thread(target=while_test, args=("/dev/ttyUSB1",2,9))
t1.start()
t2.start()
t1.start()
t1.join()
t2.join()