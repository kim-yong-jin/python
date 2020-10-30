

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.Qt import QMainWindow, QApplication



form_class = uic.loadUiType("omok.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
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
        
        self.lbl2D = []
       
        for i in range(10) :
            line = []
           
            for j in range(10):
                label = QtWidgets.QLabel(self)
                label.setGeometry(QtCore.QRect(j*40,i*40,40,40))
                label.setPixmap(QtGui.QPixmap("0.png"))
                line.append(label)
                j +=1
            self.lbl2D.append(line)
            i += 1
            
        
        
        
       
        self.pb.clicked.connect(self.btn_clicked)
        self.myrender()
    

    def btn_clicked(self):
        self.printArr2D()
            
            
    def printArr2D(self):        
        for i in self.arr2D:
            print(i)
    
    
    def myrender(self):
        
      
        
        for i in range(10):
            
            for j in range(10):
                if self.arr2D[i][j] == 0 :
                    self.lbl2D[i][j].setPixmap(QtGui.QPixmap("0.png"))
                if self.arr2D[i][j] == 1 :
                    self.lbl2D[i][j].setPixmap(QtGui.QPixmap("1.png"))    
                if self.arr2D[i][j] == 2 :
                    self.lbl2D[i][j].setPixmap(QtGui.QPixmap("2.png"))
                
           

                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
