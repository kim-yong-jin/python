import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.Qt import QMessageBox


form_class = uic.loadUiType("pyqt5.ui")[0] 


class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        
        pblist = [self.pb,self.pb_2, self.pb_3,self.pb_4,self.pb_5, self.pb_6, self.pb_7,
                  self.pb_8, self.pb_9,self.pb_10]
        self.pb_11.clicked.connect((self.btn_clicked11)) #call button
        self.pb_12.clicked.connect((self.btn_clicked12)) #reset button

        
        for i in pblist :
            i.clicked.connect(self.btn_clicked)
            
            
    def btn_clicked(self) :
        value1 = self.sender()
        value2 = value1.text()
        value3 = self.ln.text()
        self.ln.setText(value3 +value2)
                   
    def btn_clicked11(self):
        QMessageBox.about(self, "message", self.ln.text()+"님 에게 전화를 겁니다")
        
    def btn_clicked12(self):
        num = ""
        self.ln.setText(num)
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()