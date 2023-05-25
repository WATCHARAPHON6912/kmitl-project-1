import socket
import keyboard as kb
class TCP():  
    def init_cl(self,ip,port):
        self.client_socket = socket.socket()
        self.client_socket.connect((ip, port)) 
        print("init")

    def cl_send(self,text):
        self.client_socket.send(text.encode())  

    def cl_recv(self):
        data = self.client_socket.recv(1024).decode()  
        # print(self.client_socket.getsockname())
        if data == "0":
            data=None
        return data
    def cl_close(self):
        self.client_socket.close()

    def cl_get_getsockname(self):
        return self.client_socket.getsockname()
    
###################################################################
    def init_sv(self,ip,port):
        self.server_socket = socket.socket()
        self.server_socket.bind((ip, port))
        self.server_socket.listen(2)
        self.conn, address = self.server_socket.accept()
        print("Connection from: " + str(address))

    def sv_get_getsockname(self):
        return self.server_socket.getsockname()
    
    def sv_send(self,text):
        
        self.conn.send(text.encode())

    def sv_recv(self):
        return self.conn.recv(1024).decode()
    
    def sv_close(self):
        self.conn.close()

if __name__ == '__main__':
    joint1 = 400
    joint2 = 90
    joint3 = 90
    joint4 = 0
    j1=True
    j2=True
    j3=True
    while 1:
        try:
            import time
            
            s = TCP()
            s.init_sv("192.168.31.171",8080)
        
            while 1:
                if j1:joint1 += 1
                else:joint1 -= 1
                if joint1 >= 400:j1 = False
                if joint1 <= 100 :j1 = True

                if j2:joint2 += 1
                else:joint2 -= 1
                if joint2 >= 180:j2 = False
                if joint2 <= 0 :j2 = True

                if j3:joint3 += 1
                else:joint3 -= 1
                if joint3 >= 180:j3 = False
                if joint3 <= 0 :j3 = True

                joint4 += 1
                if joint4 >= 90:joint4=0


                s.sv_send(f"{joint1},{joint2},{joint3},{joint4},{joint3},{joint3},{joint3},{joint3},{1}")
                time.sleep(0.01)
                if kb.is_pressed("q"):
                    break
            
            # con = ""
            #while 1:
            #    print(s.cl_recv(),s.cl_get_getsockname())
            
            # # print("break",con)
            s.cl_close()
        except:print("server restart")
        if kb.is_pressed("q"):
            break