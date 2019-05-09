from serial_mode import *
from multiprocessing.dummy import Pool as ThreadPool


def m_add(args):
    a = args[0]
    b = args[1]
    print("called"+str(a))
    return a+b

if __name__ == '__main__':
    stamp = str(random.randint(1000,9999))
    ser1 = serial.Serial("/dev/ttyUSB3", 115200, timeout=100)
    ser2 = serial.Serial("/dev/ttyUSB6", 115200, timeout=100)
    ser3 = serial.Serial("/dev/ttyUSB5", 115200, timeout=100)
    pool = ThreadPool(3)
    # result = pool.map(serial_mode,[("/dev/ttyUSB3", 6,1,stamp),("/dev/ttyUSB6", 6, 3,stamp),("/dev/ttyUSB5", 6, 4,stamp)])
    # result = pool.map(m_add,[(1,2),(3,4),(5,6)])
    while True:
        result = pool.map(serial_mode,[(ser1, 3,1,stamp),(ser2, 3, 3,stamp),(ser3, 3, 4,stamp)])
        print('\r'+str(result[0][0]),end = '')
    pool.close()
    pool.join()