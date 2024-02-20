import sys
import glob
import serial
import struct
import crc16



def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            if port == "COM2":
                print("no jest dostepny port com2")

                result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())
    #x = 0b10100100

    #x = x >>2

    #print(bin(x))
    #n = -2
    #array = n.to_bytes(2, byteorder='big', signed=True)
    #print(array)
    message = [0x07, 0x06, 0x00, 0xC8, 0x00, 0x80]
    x = message[: 4]
    print(x)

