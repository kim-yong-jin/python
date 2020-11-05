import time
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow 
import threading
import time
from datetime import  datetime


 
 
  
form_class = uic.loadUiType("myqtThread.ui")[0] 


class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb2.clicked.connect((self.btn_clicked_start))
        self.pb.clicked.connect((self.btn_clicked_end))
        
        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
        self.browser.get("https://finance.daum.net/quotes/A005930#home")
        
        time.sleep(3)
      
        self.conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')

        self.curs = self.conn.cursor()
        
        self.flag_ing = True
    def btn_clicked_start(self):
        t = threading.Thread(target=myrun, args=(1,100000))
        t.start()
    def myrun(self,a,b):
        while self.flag_ing :
            time.sleep(1)
            self.now = datetime.datetime().now()
            
            self.tag_strong = self.browser.find_element_by_css_selector("#boxSummary > div > span:nth-child(1) > span.currentB > span.numB.up > strong") 
            
            
            sql = "INSERT INTO stock (CNAME,CCODE,PRICE,GTIME) VALUES('삼성전자','005930',%s,%s)"
            self.curs.execute(sql, ("3"))
            self.conn.commit()
        print("btn_start")
        
    def btn_clicked_end(self):
        self.flag_ing = False
        print("btn_end")     
          
    def __del__(self):
        self.conn.close()
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()