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
    return abs(a-b)

if __name__ == '__main__':
    stamp = str(random.randint(1000,9999))
    ser1 = serial.Serial("/dev/ttyUSB0", 115200, timeout=100)
    ser2 = serial.Serial("/dev/ttyUSB1", 115200, timeout=100)
    ser3 = serial.Serial("/dev/ttyUSB2", 115200, timeout=100)
    ser4 = serial.Serial("/dev/ttyUSB3", 115200, timeout=100)
    pool = ThreadPool(3)
    # result = pool.map(serial_mode,[("/dev/ttyUSB3", 6,1,stamp),("/dev/ttyUSB6", 6, 3,stamp),("/dev/ttyUSB5", 6, 4,stamp)])
    # result = pool.map(m_add,[(1,2),(3,4),(5,6)])
    scala_set = deque(maxlen=20)
    sensor_avr = [0,0,0]
    flag = ['wait','wait','wait','wait']
    while True:
        result = pool.map(serial_mode,[(ser1, 3,1,stamp),(ser2, 3, 3,stamp),(ser3, 3, 4,stamp),(ser4, 3, 2,stamp)])

        sensor_scala = []

        for i in range(4):
            sensor_data = result[i][0][0]
            sensor_scala_temp = 0
            for k,v in sensor_data.items():
                sensor_scala_temp += v*v
            sensor_scala.append(math.sqrt(sensor_scala_temp))
        scala_set.append(sensor_scala)
        
        sensor_dist_origin = [0,0,0]
        if len(scala_set) in range(2,21):
            sensor_avr_temp = []
            for m in range(4):
                avr_temp = 0
                for n in range(len(scala_set)):
                    avr_temp += scala_set[n][m]
                sensor_avr_temp.append(avr_temp/len(scala_set))
            sensor_dist_origin = [abs(sensor_avr[i] - sensor_avr_temp[i]) for i in range(len(sensor_avr))]
            sensor_avr = sensor_avr_temp
        
        for f in range(len(sensor_dist_origin)):
            if sensor_dist_origin[f] > 0.009:
                flag[f] = 'doing'
            else:
                flag[f] = 'wait'

        print('\r'+'a1:'+str(flag[0])+' a2:'+str(flag[1])+' a3:'+str(flag[2])+' a4:'+str(flag[3]),end = '',flush=True)
    pool.close()
    pool.join()