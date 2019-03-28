# -*- coding: utf-8-*-
import struct
import serial


ser = serial.Serial("/dev/sensor1", 115200, timeout=100)
if not ser.isOpen:
    ser.open()

raw_data_ac = []
raw_data_aw = []
raw_data_an = []
count = 297

while count != 0:
    flag = ser.read(1)
    flag_data = struct.unpack('<b',flag)
    if hex(flag_data[0]) == '0x55':
        raw_data = ser.read(10)
        raw_data_list = list(struct.unpack('<10b',raw_data))
        if hex(raw_data_list[0]) == '0x51':
            raw_data_ac_unit = dict(
                raw_data_ac_x=(((raw_data_list[2]) << 8) | raw_data_list[1]) / 32768 * 16,
                raw_data_ac_y=(((raw_data_list[4]) << 8) | raw_data_list[3]) / 32768 * 16,
                raw_data_ac_z=(((raw_data_list[6]) << 8) | raw_data_list[5]) / 32768 * 16
            )
            raw_data_ac.append(raw_data_ac_unit)
        elif hex(raw_data_list[0]) == '0x52':
            raw_data_aw_unit = dict(
                raw_data_aw_x=(((raw_data_list[2]) << 8) | raw_data_list[1]) / 32768 * 2000,
                raw_data_aw_y=(((raw_data_list[4]) << 8) | raw_data_list[3]) / 32768 * 2000,
                raw_data_aw_z=(((raw_data_list[6]) << 8) | raw_data_list[5]) / 32768 * 2000,
            )
            raw_data_aw.append(raw_data_aw_unit)
        elif hex(raw_data_list[0]) == '0x53':
            raw_data_an_unit = dict(
                raw_data_an_x=(((raw_data_list[2]) << 8) | raw_data_list[1]) / 32768 * 180,
                raw_data_an_y=(((raw_data_list[4]) << 8) | raw_data_list[3]) / 32768 * 180,
                raw_data_an_z=(((raw_data_list[6]) << 8) | raw_data_list[5]) / 32768 * 180,
            )
            raw_data_an.append(raw_data_an_unit)

    count = count - 1

erer = 3

with open('data_ac'+str(erer)+'.txt', 'a+') as data_ac_f:
    for data_ac_f_index in range(len(raw_data_ac)):
        data_ac_f.write(str(raw_data_ac[data_ac_f_index]) + '\n')

with open('data_an.txt', 'a+') as data_an_f:
    for data_an_f_index in range(len(raw_data_an)):
        data_an_f.write(str(raw_data_an[data_an_f_index]) + '\n')

with open('data_aw.txt', 'a+') as data_aw_f:
    for data_aw_f_index in range(len(raw_data_aw)):
        data_aw_f.write(str(raw_data_aw[data_aw_f_index]) + '\n')