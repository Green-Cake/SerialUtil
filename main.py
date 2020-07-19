# python3
# Serial Utility for twelite, cansat.
# extended format used.

import serial


SER_HEADER = bytearray([0xA5, 0x5A])


def main():
    print("program started.")

    res = 0x19  # anything is okay.
    addr = 0x02  # for relay
    data = bytearray([0xFA])  # set data here
    portid = 'COM??'  # set port id here

    srl = serialize(command(res, addr, data))

    port = serial.Serial(port=portid, baudrate=9600)
    port.write(srl)
    port.close()

    print("output:")

    for s in srl:
        print(hex(s))


# responceid: byte
# addr: byte
def command(responceid: int, addr: int, data: bytearray):
    result = bytearray([0x80, 0xA0, responceid, 0, 0, 0, addr, 0xFF])
    result += data
    return result


# command -> serialize -> output
# data: bytearray
def serialize(data):
    result = bytearray()
    result += SER_HEADER  # header
    result += bytearray([0x80, len(data)])
    result += data
    result += checksum(data)
    return result


def checksum(data: bytearray):
    a = 0
    for d in data:
        a ^= d
    return bytearray([a])


if __name__ == '__main__':
    main()
