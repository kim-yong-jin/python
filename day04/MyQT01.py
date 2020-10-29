import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow 


form_class = uic.loadUiType("hello.ui")[0] 


class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
      
        self.pb.clicked.connect((self.btn_clicked))
    def btn_clicked(self):
        self.lbl.setText("든든하지않다")
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()