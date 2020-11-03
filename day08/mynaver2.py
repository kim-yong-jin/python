import os
import sys
import urllib.request
import requests
from bs4 import BeautifulSoup
import pymysql
import re

conn = pymysql.connect(host='localhost', user='root', password='java',
                        db='python', charset='utf8')

client_id = "G_sX4slTTCXNYJYySNWT"
client_secret = "TNZUZLg5eQ"
encText = urllib.parse.quote("대전맛집")
#url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    soup = BeautifulSoup(response_body.decode('utf-8'),'lxml')
   
    curs = conn.cursor()
    
    sql = "INSERT INTO foodstore (Title,Link,description,bloggername,bloggerlink,postdate) VALUES(%s,%s,%s,%s,%s,%s)"
    
    for p in soup.find_all("item"):
        Title = p.select("title")[0].text
        
        
        link = p.select("link")[0].text
        
        
        description = p.select("description")[0].text
      
        
        bloggername = p.select("bloggername")[0].text
       
        
        bloggerlink = p.select("bloggerlink")[0].text
       
        
        postdate = p.select("postdate")[0].text
        
        print(Title)
        print(link)
        print(description)
        print(bloggername)
        print(bloggerlink)
        print(postdate)
        
        curs.execute(sql,(Title,link,description,bloggername,bloggerlink,postdate))
    conn.commit()
    conn.close()

    
    
else:
    print("Error Code:" + rescode)
    



