import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow 
import threading
import time


form_class = uic.loadUiType("myqtThread.ui")[0] 


class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect((self.btn_clicked))
        
    def btn_clicked(self):
        t = threading.Thread(target=self.myrun, args=(1,100000))
        t.start()
       
            
    def myrun(self,a,b):
        for i in range(9) :
            time.sleep(1)
            a = self.lbl.text()
            b = int(a)
            b += 1
            self.lbl.setText(str(b))
    
   
       
     
    
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
   