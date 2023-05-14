from pyModbusTCP.client import ModbusClient

class ModbusTCP():
    def __init__(self,ip,port):
        self.c = ModbusClient(host=ip,port=port,debug=False, auto_open=True)
    def write(self,addr,data):
        self.c.write_single_register(addr,data)
    def read(self,start_addr,end_addr):
        return self.c.read_holding_registers(start_addr, end_addr)

if __name__ == "__main__":
    Modbus = ModbusTCP("192.168.229.71",502)
    print(Modbus.read(0,1))
    # Modbus.write(1,666)
    # print(Modbus.read(0,9))
