import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='java',
                        db='python', charset='utf8')



url = "http://localhost/Javascript1/list.html" 


response = requests.get(url)
response.encoding = "UTF-8"
#print("status code :", response.status_code)
#print("response :", response.text)


soup = BeautifulSoup(response.text,'lxml')

curs = conn.cursor()

sql = "INSERT INTO japanlist (jname,jadress) VALUES(%s,%s)"



for p in soup.find_all("tr"):
    jname = p.select("td")[0].text
    jadress = p.select("td")[1].text
    print(jname)
    print(jadress)
    curs.execute(sql,(jname,jadress))
    
conn.commit()
conn.close()