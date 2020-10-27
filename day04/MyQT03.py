import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow 


form_class = uic.loadUiType("pyqt3.ui")[0] 


class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect((self.btn_clicked))
        
    def btn_clicked(self):
       
        temp1 = int(self.value1.text()) 
        
        temp2 = int(self.value2.text())
        
        
        
        
        temp3 = temp1 + temp2
        
        self.value3.setText(str(temp3))
        
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()