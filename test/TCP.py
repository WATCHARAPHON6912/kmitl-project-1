import socket

class TCP():  
    def init_cl(self,ip,port):
        self.client_socket = socket.socket()
        self.client_socket.connect((ip, port)) 
        print("init")

    def cl_send(self,text):
        self.client_socket.send(text.encode())  

    def cl_recv(self):
        data = self.client_socket.recv(1024).decode()  
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
    s = TCP()
    s.init_sv("192.168.229.171",8080)
    print(s.sv_get_getsockname())
    while 1:
        x = s.sv_recv()
        if x != "":
            print(x)
    s.sv_close()
        # s.sv_send("OK")
    # print("break",con)
        