import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow 


form_class = uic.loadUiType("pyqt4.ui")[0] 


class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect((self.btn_clicked))
        
    def btn_clicked(self):
        num1 = int(self.value1.text())
        num2 = int(self.value2.text())
      
        temp = 0
        
        for i in range(num1, num2+1) :
            
                temp += i
            
        self.value3.setText(str(temp));
    
       
        
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()