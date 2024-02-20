import sys
import glob
import serial
import numpy

s = serial.Serial("COM2")
s.baudrate = 9600
s.parity = serial.PARITY_NONE
s.bytesize =serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
s.timeout = 10
#info = s.read(6)

#print(info)
#print(type(info))
#print(info[5])

message = [0x07, 0x06, 0x00, 0xC8, 0x00, 0x80, 0x09, 0x67]
message2 = [0x07, 0x03, 0x00, 0x0A, 0x00, 0x01, 0xe4, 0x6f]


message = numpy.ones(8)
message3 = [7, 3, 0 , 1 , 0 ,10 ,1, 2]

x = s.write(message2)
print(" wysylane ", x)
#for i in message:
#    s.write(i)
#   print(hex(i))
#s.write(serial.STOPBITS_ONE)
y = s.read(10)

for i in range(7):

    print(y[i])




#print(" raw recall", y)
#print("type of recall ", type(y))


