from serial_mode import *
from multiprocessing.dummy import Pool as ThreadPool
import math
from collections import deque
import numpy as np
from sklearn import svm
from sklearn.externals import joblib


def dist(args):
    a = args[0]
    b = args[1]
    # print("called"+str(a))
    return abs(a - b)


if __name__ == '__main__':
    stamp = str(random.randint(1000, 9999))
    ser1 = serial.Serial("/dev/ttyUSB0", 115200, timeout=100)
    ser2 = serial.Serial("/dev/ttyUSB1", 115200, timeout=100)
    ser3 = serial.Serial("/dev/ttyUSB2", 115200, timeout=100)
    ser4 = serial.Serial("/dev/ttyUSB3", 115200, timeout=100)
    ser5 = serial.Serial("/dev/ttyUSB4", 115200, timeout=100)
    pool = ThreadPool(5)
    # result = pool.map(serial_mode,[("/dev/ttyUSB3", 6,1,stamp),("/dev/ttyUSB6", 6, 3,stamp),("/dev/ttyUSB5", 6, 4,stamp)])
    # result = pool.map(m_add,[(1,2),(3,4),(5,6)])
    scala_set = deque(maxlen=20)
    sensor_avr = [0, 0, 0, 0, 0]
    # flag = ['wait','wait','wait','wait']
    while True:
        #m_input = int(input("please input a:"))
        print("wai")
        # while m_input == 1:
        print("nei")
        result = pool.map(serial_mode, [(ser1, 35, 1, stamp), (ser2, 35, 2, stamp), (
            ser3, 35, 3, stamp), (ser4, 35, 4, stamp), (ser5, 35, 5, stamp)])
        # result contains of [different process][different sensor][dict of each time sampling]
        model1 = joblib.load("../test1.m")
        sensor_scala = []
        # temp = deque(2)
        output_mean = []
        for i in range(5):
            output = []

            sensor_data = result[i][0]
            sensor_arr = np.array(sensor_data)
            for v in sensor_data:
                output.append(v['raw_data_ac_x'])
            output = np.array(output[:380])
            # output = output.astype('float64')
            print(str(output.shape) + "   " + str(i))
            output_mean_single = np.mean(output)
            output_mean.append(output_mean_single)
            # print(output_mean)

        # temp.append(output)
        output_mean = np.array(output_mean)
        print(output_mean)
        predicted = model1.predict(output_mean.reshape(-1, 5))
        print(predicted)
        m_input = 0
        # print('\r'+'a1:'+str(flag[0])+' a2:'+str(flag[1])+' a3:'+str(flag[2])+' a4:'+str(flag[3])+' a5:'+str(flag[4]),end = '',flush=True)
    pool.close()
    pool.join()
