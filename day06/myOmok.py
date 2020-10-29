

import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication, QGridLayout, QPixmap, QLabel


form_class = uic.loadUiType("omok.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        
        self.arr2D = [[0,0,0,0,2,  0,0,0,0,2],
                      [0,1,0,0,0,  0,1,0,0,0],
                      [0,0,0,0,0,  0,0,0,0,0],
                      [0,0,1,0,0,  0,0,0,0,0],
                      [0,0,0,0,0,  0,0,0,0,0],
                      
                      [0,0,0,0,0,  0,0,0,0,0],
                      [0,0,0,0,0,  0,0,0,0,0],
                      [0,0,0,0,0,  0,0,0,0,0],
                      [0,0,0,0,0,  0,0,0,0,0],
                      [0,0,0,0,0,  0,0,0,0,0]]
        
        self.setupUi(self)
        
        
        self.pb.clicked.connect(self.btn_clicked)
        self.myrender()
    

    def btn_clicked(self):
        self.printArr2D()
            
            
    def printArr2D(self):        
        for i in self.arr2D:
            print(i)
    
    
    def myrender(self):
        
        for i in range(0,10):
            
            for j in range(0,10):
                lbl_img = QLabel() # 새로운 객체 생성
                
                if self.arr2D[i][j] == 0 :
                    lbl_img.setPixmap(self.lbl1.pixmap())  # 바둑판
                elif self.arr2D[i][j] == 1 :
                    lbl_img.setPixmap(self.lbl2.pixmap())  # 수지
                elif self.arr2D[i][j] == 2 :
                    lbl_img.setPixmap(self.lbl3.pixmap())  # 남주혁
                self.gridLayout.addWidget(lbl_img, i, j)   # 생성된 객체를 레이아웃안에 넣는다 



                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
