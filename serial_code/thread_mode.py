import threading,time
import serial_mode



thread_list = []
t1 = threading.Thread(target=serial_mode, args=("/dev/ttyUSB0",1,9))
t2 = threading.Thread(target=serial_mode, args=("/dev/ttyUSB1",2,9))
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
t1.join()
t2.join()

