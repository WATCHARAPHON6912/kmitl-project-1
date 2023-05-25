from PyQt6.QtCore import pyqtSlot, QObject, QUrl, pyqtSlot,QAbstractListModel, Qt, QModelIndex
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QMessageBox
import sys,cv2,threading,time


import Python_Lib.video as video

import Python_Lib.TCP as TCP
import Python_Lib.modbus_cl as Modbus
import Python_Lib.xlxs as xlxs
class Main(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m1 = TCP.TCP()
        self._name = "dqwd qwd"
        self._na= "h"
        self.m1_mode = 0
        
    joint1 = 230
    joint2 = 0
    joint3 = 0
    joint4 = 0
    j1=True
    j2=True
    j3=True
    re_ac = ""
    con_plc,con_m1,con_camera = False,False,False
    def map(self,x, in_min, in_max, out_min, out_max):

        re=  ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
        return int(re)
   
    @pyqtSlot(str)
    def send_re_ac(self,ra):
        self.re_ac = ra
        # if self.con_m1:
        # print(ra)
        # if ra[0] =="1" or ra[1] =="1":
            # print(ra)/
        # self.m1.cl_send("")

    i = 0
    period = 3
    last_time = 0
    i1 = 0
    period1 = 3
    last_time1 = 0
    IO1 = "1"
    IO = "1"
    @pyqtSlot(bool)
    def mode_m1(self,mode):
        move_reject = [
                [400,0,200],
                [147 ,-333, 200],
                [147, -333, 124],
                [147, -333, 200],
                [201 ,313, 200],
                [201 ,313, 128]
                ]
        move_accep = [
                [400,0,200],
                [147 ,-333, 200],
                [147, -333, 124],
                [147, -333, 200],
                [400,0,200],
                [400 ,0, 128]
                ]

        if mode != self.m1_mode:
            self.m1_mode = mode
            # print(self.i)
        if mode == False:
            print(self.re_ac)
            if self.re_ac == "01":
                
                if (int(time.time()) - self.last_time1) > self.period1 :
                    self.last_time1 = int(time.time())
                    if self.i1>=len(move_accep):self.i1=0
                    try:
                        if self.i1==3:
                            self.IO1 = "0"
                        if self.i1==(len(move_accep)-1):
                            self.IO1 = "1"
                        time.sleep(0.1)
                        self.m1.cl_send(f"ptp {move_accep[self.i1][0]} {move_accep[self.i1][1]} {move_accep[self.i1][2]} {self.IO1}")
                        
                    
                    except:pass
                    self.i1+=1

            if self.re_ac == "10":
                if (int(time.time()) - self.last_time) > self.period :
                    self.last_time = int(time.time())
                    if self.i>=len(move_reject):self.i=0
                    try:
                        if self.i==3:
                            self.IO = "0"
                        if self.i==(len(move_reject)-1):
                            self.IO = "1"
                        self.m1.cl_send(f"ptp {move_reject[self.i][0]} {move_reject[self.i][1]} {move_reject[self.i][2]} {self.IO}")
                    except:pass
                    self.i+=1
            # print(self.i)

    @pyqtSlot(result=int)
    def joint1_loop(self):
        j1 = self.map(self.joint1,15,230,100,400) #j1
        
        return j1
    
    @pyqtSlot(result=int)
    def joint2_loop(self):
        j2 = self.map(self.joint2,-80,90,0,180) #j2
        return j2
    
    @pyqtSlot(result=int)
    def joint3_loop(self):
        j3 = self.map(self.joint3,-130,130,-50,230) #j3
        return j3
    
    @pyqtSlot(result=int)
    def joint4_loop(self):
        j4 = self.map(self.joint4,-130,130,-50,230) #j3
        return j4
    m_1 = 1
    m_1_on = True
    @pyqtSlot(result=str)
    def get_m1_loop(self):
        if self.con_m1:
            if self.m_1 == 1:
                self.m_1_on = True
                thr = threading.Thread(target=self.m1_run)
                thr.start()
                self.m_1 = 0
        else :
            self.m_1_on = False
            self.m_1 = 1
            try:self.m1.cl_close()
            except:pass

    
        
    def m1_run(self):
        while self.m_1_on:
            try:
                data = self.m1.cl_recv()
                joint_xyzr = data.split(",")
                
                
                self.joint1 = float(joint_xyzr[6])
                self.joint2 = float(joint_xyzr[4])
                self.joint3 = float(joint_xyzr[5])
                self.joint4 = float(joint_xyzr[7])
                # print(joint_xyzr[4:],self.joint2,self.joint3)
                # print(self.joint1,self.joint2,self.joint3)

                
            except:pass
                # print("TCP_rev_error")
                # self.m_1_on = False
                # self.m_1 = 1
                # self.con_m1 = False
                

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
        except:pass

    @pyqtSlot(str)
    def send(self, name):
        self._name= name
        self._name = str(self._name).split(" ")
        
        if name[0] == "+" or name[0] == "-":
            self.m1.cl_send(name)
            print(name)
        if self._name[0] == "camera_set" and self._name[1] == "1":self.con_camera = True
        elif self._name[0] == "camera_set" and self._name[1] == "0":self.con_camera =False
        elif self._name[0] == "camera":self.con_camera = not self.con_camera
        elif self._name[0] == "m1":
                self.con_m1 = not self.con_m1
                try:
                    if self.con_m1 == True:
                        self.m1.init_cl(self._name[1],int(self._name[2]))
                except:
                    self.messagebox("M1 Connect error")
                    # pass
                    # self.con_m1 =False
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
    def __init__(self, sheet,parent=None):
        super().__init__(parent)
        self._strings = []
        xl = xlxs.excel(sheet)
        A,B,C = xl.xlxs_read()
        A.reverse()
        B.reverse()
        C.reverse()
        
        for i in range(len(A)):
                self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
                self._strings.append(A[i]+" "+B[i]+" | "+C[i])
                self.endInsertRows()
        print(self._strings)
        try:
            del C[0]
        except:pass
        self.last_run_card = C
        

    def rowCount(self, parent=QModelIndex()):
        return len(self._strings)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount()):
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            return self._strings[index.row()]
        return None
    
    last_run_card =[]
   
    @pyqtSlot(str)
    def addString(self, string):
        
        try:
                data = string.split("*")
                run_card = data[0].split("/")
                date = data[1].split("'")
                del run_card[-1]
                del run_card[0]
                del date[0]
                # print(string)

                if run_card != self.last_run_card:
                    for i in range(len(run_card)):
                        try:
                            if run_card[i] == self.last_run_card[i]:
                                pass
                        except:
                            self.last_run_card.append(run_card[i])
                            # print("000",self.last_run_card)
                            for i in range(len(self._strings)):
                                self.removeString(self._strings[-1])
                            self._strings.clear()
                            for i in range(len(run_card)):
                                self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
                                self._strings.reverse()
                                self._strings.append(date[i]+"  |  "+run_card[i])
                                self._strings.reverse()
                                self.endInsertRows()

                            # self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
                            # self._strings.append(date[-1]+"  |  "+run_card[-1])
                            # print("hhhhh")
                            # # self._strings.insert(0,"fnkjesjfnliesf")
                            # self.endInsertRows()
        except:pass
        
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

    string_list_model = StringListModel("accept")
    engine.rootContext().setContextProperty('stringListModel', string_list_model)
    string_list_model1 = StringListModel("reject")
    engine.rootContext().setContextProperty('stringListModel1', string_list_model1)
    
    engine.addImageProvider("MyImageProvider", myImageProvider)

    engine.load(QUrl.fromLocalFile("main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    cv2.destroyAllWindows()
    sys.exit(app.exec())
    
