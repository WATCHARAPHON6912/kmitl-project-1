from PyQt6.QtCore import pyqtSlot, QObject, QUrl, pyqtSlot
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine
import sys

import Python_Lib.video as video


class Main(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._name = ""
        self._na= "h"

    joint1 = 100
    joint2 = 0
    joint3 = 0
    joint4 = 0
    j1=True
    j2=True
    j3=True
    @pyqtSlot(result=int)
    def joint1_loop(self):
        if self.j1 == True:self.joint1 += 1
        else: self.joint1 -= 1

        if self.joint1 >= 400:self.j1 = False
        if self.joint1 <= 100:self.j1 = True
        
        return self.joint1
    @pyqtSlot(result=int)
    def joint2_loop(self):
        if self.j2:self.joint2 += 1
        else:self.joint2 -= 1

        if self.joint2 >= 180:self.j2 = False
        if self.joint2 <= 0 :self.j2 = True
        return self.joint2
    @pyqtSlot(result=int)
    def joint3_loop(self):
        if self.j3:self.joint3 += 1
        else:self.joint3 -= 1

        if self.joint3 >= 180:self.j3 = False
        if self.joint3 <= 0 :self.j3 = True
        return self.joint3
    @pyqtSlot(result=int)
    def joint4_loop(self):
        self.joint4 += 1
        if self.joint4 >= 90:self.joint4=0
        return self.joint4

    @pyqtSlot(str)
    def send(self, name):
        self._name = name
        print(self._name)

    @pyqtSlot(result=str)
    def recv(self):
        print(self._na)
        return self._na


import cv2
if __name__ == "__main__":
    app = QApplication([])
    engine = QQmlApplicationEngine()

    main = Main()
    myImageProvider = video.ImageProvider()
    engine.rootContext().setContextProperty("python", main)
    engine.rootContext().setContextProperty("myImageProvider", myImageProvider)
    
    engine.addImageProvider("MyImageProvider", myImageProvider)

    engine.load(QUrl.fromLocalFile("main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
