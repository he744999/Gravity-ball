# -*- coding: utf-8 -*-
# Author: pomelo
# Pw @ 2017-09-28 13:07:39

import sys
sys.path.insert(0, "../lib")
import Leap 
import bluetooth as bt
from Tkinter import *


class Application(Frame):
    sock = bt.BluetoothSocket(bt.RFCOMM)
    
    def disconnect(self):
        # Close socket conection to device
        self.sock.close()
    
    def on(self):
        data = "H"
        self.sock.send(data)

    def off(self):
        data = "L"
        self.sock.send(data)

    def createWidgets(self):
        # Form all the buttons
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.disconnectFrom = Button(self)
        self.disconnectFrom["text"] = "Disconnect"
        self.disconnectFrom["fg"]   = "darkgrey"
        self.disconnectFrom["command"] =  self.disconnect

        self.disconnectFrom.pack({"side": "left"})

        self.turnOn = Button(self)
        self.turnOn["text"] = "On",
        self.turnOn["fg"] = "green"
        self.turnOn["command"] = self.on

        self.turnOn.pack({"side": "left"})

        self.turnOff = Button(self)
        self.turnOff["text"] = "Off" 
        self.turnOff["fg"] = "red"
        self.turnOff["command"] = self.off 
        self.turnOff.pack({"side": "left"})

    def __init__(self, target_addr, master=None):
        self.sock.connect((target_addr, 1))
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


target_addr = "20:15:05:13:59:11"
root = Tk()
app = Application(target_addr, master=root)
app.mainloop()
root.destroy()

