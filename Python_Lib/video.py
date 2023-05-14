
import cv2

from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from PyQt6.QtQuick import  QQuickImageProvider
import time,threading
try:
    from Python_Lib import Image
    from Python_Lib import xlxs
except:
    import Image
    import xlxs

img_camera = []

class Camera:
    global img_camera
    on_camera = True
        
    def camera(self,cap):
            global img_camera
            self.frame=cv2.VideoCapture(cap)
                    
            while self.on_camera:
                _,img = self.frame.read()
                # print("run")
                img_camera = img
    def start(self,cp):
        thr = threading.Thread(target=self.camera,args=[cp])
        thr.start()
    def stop(self):
                 
        self.on_camera = False
        time.sleep(0.1)
        try:
            self.frame.release()
        except:pass
        cv2.destroyAllWindows()
        print("###########################################################################")

class ThreadCamera(QThread):
    
    updateFrame = pyqtSignal(QImage)
    cap = cv2.VideoCapture(0)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
    
    def run(self):
        while 1:
            try:
                ret, frame = self.cap.read()
                if not ret:
                    img = QImage("./images/network.png")
                    self.updateFrame.emit(img)
                # frame = cv2.imread("image.jpg")
                color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = QImage(color_frame.data, color_frame.shape[1], color_frame.shape[0], QImage.Format.Format_BGR888)
                self.updateFrame.emit(img)
            except:pass



class ImageProvider(QQuickImageProvider):
    global img_camera
    imageChanged = pyqtSignal(QImage)
    last_runcard = []
    runcard = []
    # cp = cv2.VideoCapture(1)
    def __init__(self):
        super(ImageProvider, self).__init__(QQuickImageProvider.ImageType.Image)

        self.cam = ThreadCamera() 
        self.cam.updateFrame.connect(self.update_image)
        self.image = None
        self.status_cam = False
        self.run_card = [""]
        self.last_run_card = []

    def requestImage(self, id, size):
        if self.image:
            img = self.image
        else:
            img = QImage(600, 500, QImage.Format.Format_RGBA8888)
            img.fill(Qt.GlobalColor.black)

        return img,img.size()
    @pyqtSlot(result=str)
    def get_runcard_on(self):
        if self.status_cam:
            if self.run_card != self.last_run_card:
                for i in range(len(self.run_card)):
                    try:
                        if self.run_card[i] == self.last_run_card[i]:
                            # print("OK")
                            pass
                    except:
                        self.last_run_card.append(self.run_card[i])
                        print("add",self.last_run_card)
            x=""
            for i in self.last_run_card:
                x = x+i+" " 
            return x
            # return str(self.on)+" "+self.run_card[-1]
        else:return "0"
        # if self.status_cam:
        #     return str(self.on)+" "+self.run_card[-1]
        # else:return "0 0"

    
    Excel = xlxs.excel()
    @pyqtSlot()
    def update_image(self):
        # print(time.time()-self.x)
        # self.x=time.time()
        if self.status_cam:
            # try:
                # _,color_frame = self.cp.read()
                color_frame = img_camera

                color_frame,rrr=Image.image(color_frame)
                self.run_card = self.Excel.xlxs_write(rrr)


                # if self.run_card[-1] != self.last_run_card[-1]:
                #     print("ndhjwabdjk")
                #     self.last_run_card = self.run_card
                    
                # if (rrr in self.run_card) == False and rrr != "0":
                #     if self.run_card != self.last_run_card:
                #         self.run_card = xlxs.xlxs_data(rrr)
                #         print(self.run_card)

                # print("runcard ",runcard)

                img = QImage(color_frame.data, color_frame.shape[1], color_frame.shape[0], QImage.Format.Format_BGR888)
                self.imageChanged.emit(img)
                # img = QImage(600, 500, QImage.Format.Format_RGBA8888)
                # img.fill(Qt.GlobalColor.red)
                # self.imageChanged.emit(img)
               

                self.image = img
            # except:
                # self.cam.exec()
        else:
            img = QImage(600, 500, QImage.Format.Format_RGBA8888)
            img.fill(Qt.GlobalColor.transparent)
            self.imageChanged.emit(img)
            self.image = img


    @pyqtSlot(result=int)
    def get_camera_accept(self):
        return self.camera_status
        # return False
    def messagebox(self,text):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("App")
        self.msg.setText(text)
        self.msg.exec()

    @pyqtSlot(str)
    def start(self,camera):
        print("Starting...")
        try:
            if len(camera)<=2:
                if int(camera) < len(self.returnCameraIndexes()):
                    self.x=Camera()
                    self.x.start(int(camera))
                    print("Starting...")
                    self.cam.start()
                    self.camera_status = 1
                else:
                    self.messagebox("Not Connect Webcam chack IP ro PORT")
                    self.camera_status = 0

            else:
                try:
                    self.x=Camera()
                    self.x.start(camera)
                    self.cam.start()
                except:pass
                self.camera_status = 3
        except:self.messagebox("Not Connect Webcam chack IP ro PORT")

            
    @pyqtSlot()
    def no_exit(self):
        print("exit")
        # self.killThread()
        # time.sleep(5)
        self.messagebox("All connections must be disconnected.")
 

    @pyqtSlot()
    def killThread(self):
        
        try:
            self.x.stop()
            self.cam.exec()
            print("Finishing...")
            cv2.destroyAllWindows()
        except:
            pass

    @pyqtSlot(bool)
    def get_cam(self,cam):
        self.status_cam = cam
        # print(self.status_cam)

    def returnCameraIndexes(self):
        try:
            index = 0
            arr = []
            while True:
                cap = cv2.VideoCapture(index)
                try:
                    if cap.getBackendName()=="MSMF":
                        arr.append(index)
                except:
                    break
                cap.release()
                index += 1
            return arr
        except:self.messagebox("Not Connect Webcam chack IP ro PORT")

        



# class MainWindow(QObject):
#     def __init__(self):
#         QObject.__init__(self)
    

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("image.jpg"))
#     engine = QQmlApplicationEngine()

#     #Get Context
#     main = MainWindow()
#     myImageProvider = ImageProvider()
#     engine.rootContext().setContextProperty("backend", main)
#     engine.rootContext().setContextProperty("myImageProvider", myImageProvider)
    
#     engine.addImageProvider("MyImageProvider", myImageProvider)

#     #Load QML File
#     engine.load(os.fspath(Path(__file__).resolve().parent /  "main.qml"))

#     if not engine.rootObjects():
#         sys.exit(-1)
#     sys.exit(app.exec())