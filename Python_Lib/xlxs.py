from openpyxl import load_workbook
import datetime

# def xlxs_data(runcard,modbus):
class excel:
    def __init__(self):
        self.data_A = []
        self.data_B = []
        self.data_C = []
        self.xlxs_read()
    
    def xlxs_read(self):
        wb = load_workbook(filename = r'C:\Users\filmm\OneDrive\Desktop\UntitledProject\excel\xcel.xlsx')
        self.worksheet = wb['Sheet1']
        A = self.worksheet['a']
        B = self.worksheet['b']
        C = self.worksheet['c']
        self.data_A.clear()
        self.data_B.clear()
        self.data_C.clear()

        x =-1
        for i in A:
            x+=1
            self.data_A.append(str(i.value))

        x =-1
        for i in B:
            x+=1
            self.data_B.append(str(i.value)[0:10])

        x =-1
        for i in C:
            x+=1
            self.data_C.append(str(i.value))
        
        wb.close()
        return self.data_C

    def xlxs_write(self,runcard):
        date = datetime.datetime.now()
        
        if len(runcard) >5: 
            if(runcard in self.data_C):
                # modbus.write(0,0)
                # messagebox("Runcard duplicate")
                return self.data_C,0
            
            else:
                wb = load_workbook(filename = r'C:\Users\filmm\OneDrive\Desktop\UntitledProject\excel\xcel.xlsx')
                self.worksheet = wb['Sheet1']
                self.worksheet.append({'A' : str(date.strftime("%d-%m-%Y")), 'B' : str(date.strftime("%X")), 'C' : f'{runcard}'})
                wb.save(r'C:\Users\filmm\OneDrive\Desktop\UntitledProject\excel\xcel.xlsx')
                wb.close()
                self.xlxs_read()
                return self.data_C
        return self.data_C
    
if __name__ == "__main__":
    x = excel()
    for i in range(10):
        print(x.xlxs_write(f"th0000-{i}"))
