import serial
import struct
import threading
import time
import random

lock = threading.Lock()
stamp = str(random.randint(1000,9999))

# def serial_mode(sensor, count_out, order, stamp):
def serial_mode(args):
    [ser,count_out,order,stamp] = [x for x in args]
    # lock.acquire()
    # stamp = str(random.randint(1000,9999))
    # ser = serial.Serial(sensor, 115200, timeout=100)
    if not ser.isOpen:
        ser.open()

    raw_data_ac = []
    raw_data_aw = []
    raw_data_an = []
    count = 33
    for count_index in range(count_out):
        # print("data_ac" + str(count_index))
        #        count_out = count_out - 1
        for count_index_in in range(count):
            # print(order)
            # while (count >= 0):
            flag = ser.read(1)
            flag_data = struct.unpack('<b', flag)
            if hex(flag_data[0]) == '0x55':
                raw_data = ser.read(10)
                raw_data_list = list(struct.unpack('<10b', raw_data))
                if hex(raw_data_list[0]) == '0x51':
                    raw_data_ac_unit = dict(
                        raw_data_ac_x=(
                            ((raw_data_list[2]) << 8) | raw_data_list[1]) / 32768 * 16,
                        raw_data_ac_y=(
                            ((raw_data_list[4]) << 8) | raw_data_list[3]) / 32768 * 16,
                        raw_data_ac_z=(
                            ((raw_data_list[6]) << 8) | raw_data_list[5]) / 32768 * 16
                    )
                    raw_data_ac.append(raw_data_ac_unit)
                elif hex(raw_data_list[0]) == '0x52':
                    raw_data_aw_unit = dict(
                        raw_data_aw_x=(
                            ((raw_data_list[2]) << 8) | raw_data_list[1]) / 32768 * 2000,
                        raw_data_aw_y=(
                            ((raw_data_list[4]) << 8) | raw_data_list[3]) / 32768 * 2000,
                        raw_data_aw_z=(
                            ((raw_data_list[6]) << 8) | raw_data_list[5]) / 32768 * 2000,
                    )
                    raw_data_aw.append(raw_data_aw_unit)
                elif hex(raw_data_list[0]) == '0x53':
                    raw_data_an_unit = dict(
                        raw_data_an_x=(
                            ((raw_data_list[2]) << 8) | raw_data_list[1]) / 32768 * 180,
                        raw_data_an_y=(
                            ((raw_data_list[4]) << 8) | raw_data_list[3]) / 32768 * 180,
                        raw_data_an_z=(
                            ((raw_data_list[6]) << 8) | raw_data_list[5]) / 32768 * 180,
                    )
                    raw_data_an.append(raw_data_an_unit)
    return [raw_data_ac,raw_data_an,raw_data_aw]
            # count = count - 1
        # time.sleep(1)
    # print(str(order) + "done!")
'''
    with open('../data/ac/'+stamp+'data_ac_x' + str(order) + '.txt', 'w+') as data_ac_x_f, open('../data/ac/'+stamp+'data_ac_y' + str(order) + '.txt', 'w+') as data_ac_y_f, open('../data/ac/'+stamp+'data_ac_z' + str(order) + '.txt', 'w+') as data_ac_z_f:
        for data_ac_index in raw_data_ac:
            data_ac_keys = data_ac_index.keys()
            for data_ac_keys_index in data_ac_keys:
                if data_ac_keys_index == "raw_data_ac_x":
                    data_ac_x_f.write(
                        str(data_ac_index[data_ac_keys_index]) + " ")
                elif data_ac_keys_index == "raw_data_ac_y":
                    data_ac_y_f.write(
                        str(data_ac_index[data_ac_keys_index]) + " ")
                elif data_ac_keys_index == "raw_data_ac_z":
                    data_ac_z_f.write(
                        str(data_ac_index[data_ac_keys_index]) + " ")

    with open('../data/aw/'+stamp+'data_aw_x' + str(order) + '.txt', 'w+') as data_aw_x_f, open('../data/aw/'+stamp+'data_aw_y' + str(order) + '.txt', 'w+') as data_aw_y_f, open('../data/aw/'+stamp+'data_aw_z' + str(order) + '.txt', 'w+') as data_aw_z_f:
        for data_aw_index in raw_data_aw:
            data_aw_keys = data_aw_index.keys()
            for data_aw_keys_index in data_aw_keys:
                if data_aw_keys_index == "raw_data_aw_x":
                    data_aw_x_f.write(
                        str(data_aw_index[data_aw_keys_index]) + " ")
                elif data_aw_keys_index == "raw_data_aw_y":
                    data_aw_y_f.write(
                        str(data_aw_index[data_aw_keys_index]) + " ")
                elif data_aw_keys_index == "raw_data_aw_z":
                    data_aw_z_f.write(
                        str(data_aw_index[data_aw_keys_index]) + " ")
    with open('../data/an/'+stamp+'data_an_x' + str(order) + '.txt', 'w+') as data_an_x_f, open('../data/an/'+stamp+'data_an_y' + str(order) + '.txt', 'w+') as data_an_y_f, open('../data/an/'+stamp+'data_an_z' + str(order) + '.txt', 'w+') as data_an_z_f:
        for data_an_index in raw_data_an:
            data_an_keys = data_an_index.keys()
            for data_an_keys_index in data_an_keys:
                if data_an_keys_index == "raw_data_an_x":
                    data_an_x_f.write(
                        str(data_an_index[data_an_keys_index]) + " ")
                elif data_an_keys_index == "raw_data_an_y":
                    data_an_y_f.write(
                        str(data_an_index[data_an_keys_index]) + " ")
                elif data_an_keys_index == "raw_data_an_z":
                    data_an_z_f.write(
                        str(data_an_index[data_an_keys_index]) + " ")
'''
    # lock.release()
    # return raw_data_ac



if __name__ == '__main__':
    '''
    t1 = threading.Thread(target=serial_mode, args=("com16", 3, 1))
    t2 = threading.Thread(target=serial_mode, args=("com17", 3, 2))
    '''
    t1 = threading.Thread(target=serial_mode, args=("/dev/ttyUSB3", 6,1,stamp))
    # t2 = threading.Thread(target=serial_mode, args=("/dev/ttyUSB2", 6, 2,stamp))
    t3 = threading.Thread(target=serial_mode, args=("/dev/ttyUSB6", 6, 3,stamp))
    t4 = threading.Thread(target=serial_mode, args=("/dev/ttyUSB5", 6, 4,stamp))
    # t1.setDaemon(True)
    # t2.setDaemon(True)
    t1.start()
    # t2.start()
    t3.start()
    t4.start()
    t1.join()
    # t2.join()
    t3.join()
    t4.join()


