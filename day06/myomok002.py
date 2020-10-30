from os.path import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtWidgets

from PyQt5.Qt import QSize
from dask.dataframe.tests.test_rolling import idx
from sqlalchemy.dialects.mssql.base import try_cast

from_class = uic.loadUiType("omok.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.arr2D = [
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]
                    ]
        self.setupUi(self)
        self.btn2D = []
        self.flagturn = True
        for i in range(len(self.arr2D)):
            line = []
            for j in range(len(self.arr2D[i])):
                btn = QtWidgets.QPushButton(self)
                btn.setAccessibleName(str(i)+"," + str(j))
                btn.setGeometry(j*40, i*40, 40, 40)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QSize(40,40));
                btn.clicked.connect(self.btn_clicked)
                line.append(btn)
            self.btn2D.append(line)
        
        
    def myrender(self):
        for i in range(len(self.arr2D)):
            for j in range(len(self.arr2D[i])):
                if self.arr2D[i][j]==0 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("0.png"))
                elif self.arr2D[i][j]==1 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("1.png"))
                elif self.arr2D[i][j]==2 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("2.png"))
    
   
            
    def btn_clicked(self):
        txt = self.sender().accessibleName()
        ijinfo = txt.split(",")
        ii = int(ijinfo[0])
        jj = int(ijinfo[1])
        
        if self.arr2D[ii][jj] > 0:
            return
        
        
        idx_stone = 0
        if self.flagturn == True:
            self.arr2D[ii][jj] = 1
            idx_stone = 1
        else :
            self.arr2D[ii][jj] = 2
            idx_stone = 2
        self.myrender()
        
        cntUp = self.getUp(ii,jj,idx_stone)
        cntDw = self.getDw(ii,jj,idx_stone)
        
        cntLe = self.getLe(ii,jj,idx_stone)
        cntRi = self.getRi(ii,jj,idx_stone)

        cntUl = self.getUl(ii,jj,idx_stone)
        cntUR = self.getUR(ii,jj,idx_stone)
#         
        cntDL = self.getDL(ii,jj,idx_stone)
        cntDR = self.getDR(ii,jj,idx_stone)
        print("cntDR : ", cntDR)
        
        self.flagturn = not self.flagturn
    def getDR(self,i,j,idx):
        cnt = 0
        try :
            while True :
                i +=1
                j +=1
                if self.arr2D[i][j] == idx :
                    cnt += 1
                else :
                    break
        except :
            pass 
        return cnt
    def getDL(self,i,j,idx):
        cnt = 0
        try :
            while True :
                i +=1
                j -=1
                if self.arr2D[i][j] == idx :
                    cnt += 1
                else :
                    break
        except :
            pass 
        return cnt
    def getUR(self,i,j,idx):
        cnt = 0
        try :
            while True :
                i -=1
                j +=1
                if self.arr2D[i][j] == idx :
                    cnt += 1
                else :
                    break
        except :
            pass 
        return cnt
    def getUl(self,i,j,idx):
        cnt = 0
        try :
            while True :
                i +=1
                j +=1
                if self.arr2D[i][j] == idx :
                    cnt += 1
                else :
                    break
        except :
            pass 
        return cnt
    def getRi(self,i,j,idx):
        cnt = 0
        try :
            while True :
                j += 1
                
                if self.arr2D[i][j] == idx :
                    cnt += 1
                else :
                    break
        except :
            pass 
        return cnt
    def getLe(self,i,j,idx):
        cnt = 0
        try :
            while True :
                j -= 1
                
                if self.arr2D[i][j] == idx :
                    cnt += 1
                else :
                    break
        except :
            pass 
        return cnt
    def getDw(self,i,j,idx):
        cnt = 0
        try :
            while True :
                i += 1
                
                if self.arr2D[i][j] == idx :
                    cnt += 1
                else :
                    break
        except :
            pass 
        return cnt
    
    
    def getUp(self,i,j,idx):
        cnt = 0;
        
        try :
            while True :
                i -= 1
                if i < 0 :
                    return cnt
                if self.arr2D[i][j] == idx :
                    cnt += 1
                else :
                    break
        except :
            pass 
        return cnt    
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
