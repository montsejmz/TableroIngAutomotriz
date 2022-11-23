import os

import can

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ip link set can0 up')

can_interface = 'can0'
bus = can.interface.Bus(channel = can_interface, bustype = 'socketcan')
while True:
    message = bus.recv()
    if message.arbitration_id == 0x36:
        print(message.data[0])
