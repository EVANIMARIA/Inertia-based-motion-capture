# -*- coding: utf-8-*-
import serial
# ser = serial.Serial("com6", 460800, timeout=100)
ser = serial.Serial("/dev/ttyUSB1", 115200, timeout=1)
if not ser.isOpen:
    ser.open()
s = ser.read(66)
raw_data = []
data = []
data_ac = dict(data_ac_x=1, data_ac_y=1, data_ac_z=1)
raw_data_ac = []
raw_data_aw = []
raw_data_an = []
for x in s:
    raw_data.append(x)
for index in range(len(raw_data)):
    if raw_data[index] == 0x55:
        data = raw_data[index:index + 10]
        if data[1] == 0x51:
            raw_data_ac_unit = dict(
                raw_data_ac_x=(((data[3]) << 8) | data[2]) / 32768 * 16,
                raw_data_ac_y=(((data[5]) << 8) | data[4]) / 32768 * 16,
                raw_data_ac_z=(((data[7]) << 8) | data[6]) / 32768 * 16
            )
            raw_data_ac.append(raw_data_ac_unit)
        elif data[1] == 0x52:
            raw_data_aw_unit = dict(
                raw_data_aw_x=(((data[3]) << 8) | data[2]) / 32768 * 2000,
                raw_data_aw_y=(((data[5]) << 8) | data[4]) / 32768 * 2000,
                raw_data_aw_z=(((data[7]) << 8) | data[6]) / 32768 * 2000,
            )
            raw_data_aw.append(raw_data_aw_unit)
        elif data[1] == 0x53:
            raw_data_an_unit = dict(
                raw_data_an_x=(((data[3]) << 8) | data[2]) / 32768 * 180,
                raw_data_an_y=(((data[5]) << 8) | data[4]) / 32768 * 180,
                raw_data_an_z=(((data[7]) << 8) | data[6]) / 32768 * 180,
            )
            raw_data_an.append(raw_data_an_unit)

with open('data_ac.txt', 'a+') as data_ac_f:
    for data_ac_f_index in range(len(raw_data_ac)):
        data_ac_f.write(str(raw_data_ac[data_ac_f_index]) + '\n')

with open('data_an.txt', 'a+') as data_an_f:
    for data_an_f_index in range(len(raw_data_an)):
        data_an_f.write(str(raw_data_an[data_an_f_index]) + '\n')

with open('data_aw.txt', 'a+') as data_aw_f:
    for data_aw_f_index in range(len(raw_data_aw)):
        data_aw_f.write(str(raw_data_aw[data_aw_f_index]) + '\n')

# print(raw_data_ac)