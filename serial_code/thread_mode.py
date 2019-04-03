import serial
import struct
import threading
import time

lock = threading.Lock()


def serial_mode(sensor, count_out, order):
    #.acquire()
    count = 3
    for count_index in range(count_out):
    	time.sleep(0.2)
    	for count_index_in in range(count):
            print(order)
    print("done!")
    #lock.release()


t1 = threading.Thread(target=serial_mode, args=("/dev/ttyUSB0", 3, 1))
t2 = threading.Thread(target=serial_mode, args=("/dev/ttyUSB1", 3, 2))
t2.start()
t1.start()
t1.join()
t2.join()