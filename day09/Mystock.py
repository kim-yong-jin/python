from bs4 import BeautifulSoup
from datetime import  datetime
import requests
import time
import pymysql
import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow 
import threading


form_class = uic.loadUiType("myqtThread.ui")[0] 


class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self) 
        self.pb.clicked.connect((self.btn_clicked))
        
        
        self.conpany_name = "삼성전자"
        self.company_codes = ["005930"]
        
        self.conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
        self.curs = self.conn.cursor()
        
        self.sql = "INSERT INTO stock (CNAME,CCODE,PRICE,GTIME) VALUES(%s,%s,%s,%s)"
        
        
        
    def btn_clicked(self):
        t = threading.Thread(target=self.myrun)
        t.start()
    
    def myrun(self):
        while True:
            now = datetime.now() 
            print (now) 
            for item in self.company_codes:
                now_price = self.get_price(item)
                print("현재가 :" ,now_price)
                print("-------------------------------")
                self.curs.execute(self.sql, (self.conpany_name,self.company_codes,now_price,now))
            time.sleep(50)
            self.conn.commit()
      
       
               
    def get_code(self,company_code):
        url = "https://finance.naver.com/item/main.nhn?code=" + company_code
        result = requests.get(url)
        bs_obj = BeautifulSoup(result.content, "html.parser") 
        return bs_obj 
    
    
    def get_price(self,company_code):
        bs_obj = self.get_code(company_code)
        no_today = bs_obj.find("p", {"class": "no_today"})
        blind = no_today.find("span", {"class": "blind"})
        now_price = blind.text 
        return now_price 
   
       
     
    
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
   















