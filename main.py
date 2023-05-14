from PyQt6.QtCore import pyqtSlot, QObject, QUrl, pyqtSlot,QAbstractListModel, Qt, QModelIndex
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QMessageBox
import sys,cv2,time
from datetime import datetime as dt


import Python_Lib.video as video

import Python_Lib.TCP as TCP
import Python_Lib.modbus_cl as Modbus
import Python_Lib.xlxs as xlxs
class Main(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._name = "dqwd qwd"
        self._na= "h"

    joint1 = 100
    joint2 = 0
    joint3 = 0
    joint4 = 0
    j1=True
    j2=True
    j3=True
    con_plc,con_m1,con_camera = False,False,False
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
    
    @pyqtSlot(result=str)
    def get_plc_loop(self):
        if self.con_plc:
            try:
                re = self.modbus.read(0,2)
                return str(re[0])+" "+str(re[1])
            except:pass
    
    @pyqtSlot(str)
    def write_plc(self,addr):
        print(addr)
        try:
            if self.con_plc:
                self.modbus.write(int(addr[0]),int(addr[1]))
                # print("jj")
        except:pass

    @pyqtSlot(str)
    def send(self, name):
        self._name= name
        self._name = str(self._name).split(" ")
        
        if self._name[0] == "camera_set" and self._name[1] == "1":self.con_camera = True
        elif self._name[0] == "camera_set" and self._name[1] == "0":self.con_camera =False
        elif self._name[0] == "camera":self.con_camera = not self.con_camera
        elif self._name[0] == "m1":
                self.con_m1 = not self.con_m1
                try:
                    if self.con_m1 == True:
                        self.m1 = TCP.TCP()
                        self.m1.init_cl(self._name[1],int(self._name[2]))
                except:
                    self.messagebox("M1 Connect error")
                    self.con_m1 =False
        elif self._name[0] == "plc":self.con_plc = not self.con_plc
        else:print(self._name[0])

        try:
            if self.con_m1 :
                self.m1.cl_send(self._name[0])
        except:
            self.messagebox("M1 Connect error")
            self.con_m1 =False

        if self.con_plc == True and self._name[0] == "plc":
            try:
                self.modbus = Modbus.ModbusTCP(self._name[1],int(self._name[2]))
                if self.modbus.read(0,1) != None:self.con_plc = True
                else:
                    self.con_plc = False
                    self.messagebox("PLC Connect error")
            except:
                self.messagebox("Please check the PLC that the ip and port are correct.")
                self.con_plc = False
        
    
    @pyqtSlot(result=bool)
    def return_m1(self):
        return self.con_m1
    
    @pyqtSlot(result=bool)
    def return_camera(self):
        return self.con_camera
    
    @pyqtSlot(result=bool)
    def return_plc(self):
        return self.con_plc

    @pyqtSlot(result=str)
    def recv(self):
        return str(self.con_m1)+" "+str(self.con_plc)+" "+str(self.con_camera)
    
    def messagebox(self,text):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("App")
        self.msg.setText(text)
        self.msg.exec()

class StringListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._strings = []
        xl = xlxs.excel()
        x = xl.xlxs_read()
        for i in range(len(x)):
            if i>0:
                self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
                self._strings.append(x[i])
                self.endInsertRows()
        # print(self._strings)

    def rowCount(self, parent=QModelIndex()):
        return len(self._strings)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount()):
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            return self._strings[index.row()]
        return None
    @pyqtSlot(str)
    def addString(self, string):
        # for i in range(1000):
        #     if i >=1:
        #         self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        #         self._strings.append(str(i))
        #         print(self._strings)
        #         # self._strings = data
        #         self.endInsertRows()
        
        dd = string.split(" ")
        try:
            del dd[-1]
            del dd[0]
        except:pass
        print(dd)
        for i in range(len(self._strings)):
            self.removeString(self._strings[-1])
        self._strings.clear()

        for i in dd:
                self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
                now = dt.now()
                date = f"{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}"
                # self._strings.append(i)
                self._strings.append(date+"  |  "+i)
                self.endInsertRows()
        # now = dt.now()
        # date = f"{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}"
        # self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        # self._strings.append(date+"  |  "+string)
        # self._strings = run
        # self.endInsertRows()
       
        


    @pyqtSlot(str)
    def removeString(self, string):
        row = self._strings.index(string)
        self.beginRemoveRows(QModelIndex(), row, row)
        del self._strings[row]
        self.endRemoveRows()

if __name__ == "__main__":
    app = QApplication([])
    engine = QQmlApplicationEngine()

    main = Main()

    myImageProvider = video.ImageProvider()
    engine.rootContext().setContextProperty("python", main)
    engine.rootContext().setContextProperty("myImageProvider", myImageProvider)

    string_list_model = StringListModel()
    engine.rootContext().setContextProperty('stringListModel', string_list_model)
    string_list_model1 = StringListModel()
    engine.rootContext().setContextProperty('stringListModel1', string_list_model1)
    
    engine.addImageProvider("MyImageProvider", myImageProvider)

    engine.load(QUrl.fromLocalFile("main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    cv2.destroyAllWindows()
    sys.exit(app.exec())
    
