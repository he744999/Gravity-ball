# -*- coding: utf-8 -*-
# Author: pomelo
# Pw @ 2017-12-14 18:22:37


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
import bluetooth as bt

bd_addr = "20:15:02:26:12:10"
port = 1


class PushButton(QWidget):
    sock = bt.BluetoothSocket(bt.RFCOMM)

    def __init__(self):
        super(PushButton, self).__init__()
        self.sock.connect((bd_addr, port))
        self.initUI()

    def initUI(self):
        self.setWindowTitle("communication by bluetooth")
        self.move(200, 300)
        self.setGeometry(400, 800, 600, 260)
        self.setWindowIcon(QIcon('2.jpg'))

        self.onLight = QPushButton(self)
        self.onLight.setText("on")
        self.onLight.clicked.connect(self.on)
        self.onLight.move(100, 100)

        self.offLight = QPushButton(self)
        self.offLight.setText("off")
        self.offLight.clicked.connect(self.off)
        self.offLight.move(200, 100)

        self.quit = QPushButton(self)
        self.quit.setText("QUIT")
        self.quit.clicked.connect(self.close)
        self.quit.move(300, 100)

        self.disconnect = QPushButton(self)
        self.disconnect.resize(100, 50)
        self.disconnect.setText("Disconnect")
        self.disconnect.setToolTip("disconnect from bluetoot")
        self.disconnect.clicked.connect(self.dis)
        self.disconnect.move(400, 100)
        self.show()

    def on(self):
        data = "PHllkP"
        self.sock.sendall(data)

    def off(self):
        data = "PLllkP"
        self.sock.sendall(data)

    def dis(self):
        self.sock.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pb = PushButton()
    sys.exit(app.exec_())
