import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.Qt import QMessageBox


form_class = uic.loadUiType("pyqt5.ui")[0] 


class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect((self.btn_clicked))
        self.pb_2.clicked.connect((self.btn_clicked2))
        self.pb_3.clicked.connect((self.btn_clicked3))
        self.pb_4.clicked.connect((self.btn_clicked4))
        self.pb_5.clicked.connect((self.btn_clicked5))
        self.pb_6.clicked.connect((self.btn_clicked6))
        self.pb_7.clicked.connect((self.btn_clicked7))
        self.pb_8.clicked.connect((self.btn_clicked8))
        self.pb_9.clicked.connect((self.btn_clicked9))
        self.pb_10.clicked.connect((self.btn_clicked10))
        self.pb_11.clicked.connect((self.btn_clicked11))
        self.pb_12.clicked.connect((self.btn_clicked12))
    def btn_clicked(self):
        num1 = self.pb.text()
        num = self.ln.text() + num1
        self.ln.setText(str(num));
        
    def btn_clicked2(self):
        num2 = self.pb_2.text()
        num = self.ln.text() + num2
        self.ln.setText(str(num))
    def btn_clicked3(self):
        num3 = self.pb_3.text()
        num = self.ln.text() + num3   
        self.ln.setText(str(num))
    def btn_clicked4(self):
        num4 = self.pb_4.text()
        num = self.ln.text() + num4   
        self.ln.setText(str(num))
    def btn_clicked5(self):
        num5 = self.pb_5.text()
        num = self.ln.text() + num5   
        self.ln.setText(str(num))
    def btn_clicked6(self):
        num6 = self.pb_6.text()
        num = self.ln.text() + num6   
        self.ln.setText(str(num))  
    def btn_clicked7(self):
        num7 = self.pb_7.text()
        num = self.ln.text() + num7   
        self.ln.setText(str(num))      
    def btn_clicked8(self):
        num8 = self.pb_8.text()
        num = self.ln.text() + num8   
        self.ln.setText(str(num)) 
    def btn_clicked9(self):
        num9 = self.pb_9.text()
        num = self.ln.text() + num9   
        self.ln.setText(str(num)) 
    def btn_clicked10(self):
        num10 = self.pb_10.text()
        num = self.ln.text() + num10   
        self.ln.setText(str(num))                      
    def btn_clicked12(self):
        num = ""    
        self.ln.setText(str(num)) 
                
    def btn_clicked11(self):
        QMessageBox.about(self, "message", self.ln.text()+"님 에게 전화를 겁니다")
        
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()