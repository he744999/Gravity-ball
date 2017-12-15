# -*- coding: utf-8 -*-
# Author: pomelo
# Pw @ 2017-09-28 13:07:39

import sys
sys.path.insert(0, "../lib")
import Leap 
import bluetooth as bt
from time import sleep 
device = ('20:15:02:26:12:10', 'HC-05')
bd_addr = device[0]
port = 1
sleep(1)


class SampleListener(Leap.Listener): 

    def on_init(self, controller):
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
            flag = b"H" if hand.is_left else b"L"
            direction = hand.direction
            a = []
            angles = [direction.pitch * Leap.RAD_TO_DEG,
            direction.roll * Leap.RAD_TO_DEG,
            direction.yaw * Leap.RAD_TO_DEG]
            for angle in angles: a.append(self.deal(angle))
            data = flag + a[0] + a[1]
            self.sock.send(data)
            print(data)
            sleep(0.1)

    def deal(self, raw_num):
        n = int(raw_num)
        if(n > 50): n = 50
        if(n < -50): n = -50
        n = n + 100
        n = chr(n)
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

