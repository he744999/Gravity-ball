# -*- coding: utf-8 -*-
# Author: pomelo
# Pw @ 2017-09-28 13:07:39

import sys
sys.path.insert(0, "../lib")
import Leap 
import bluetooth as bt 
from time import sleep 
info = '''
you need run get_mac_addr.py first to get the bluetooth mac addr
so that you can connect bluetooth module immidietely
'''
print(info)
device = ('20:15:02:26:12:10', 'HC-05')
bd_addr = device[0]
port = 1
sleep(1)


class SampleListener(Leap.Listener): def on_init(self, controller):
        self.sock = bt.BluetoothSocket(bt.RFCOMM)
        self.sock.connect((bd_addr, port))
        print("Initialized...")

    def on_connect(self, controller):
        print("Connected...")

    def on_disconnect(self, controller):
        print("Disconnected...")

    def on_exit(self, controller):
        self.sock.close()
        print("Exited...")

    def on_frame(self, controller):
        frame = controller.frame()
        for hand in frame.hands:
            headType = "Left hand" if hand.is_left else "Right hand"
            direction = hand.direction
            pitch = self.pro_data(direction.pitch * Leap.RAD_TO_DEG)
            print(pitch)
            sleep(0.09)
    
    def pro_data(self, raw_num):
        n = int(raw_num)
        if(n >50): n = 50
        if(n < -50): n -50
        return n


def main():
    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()

