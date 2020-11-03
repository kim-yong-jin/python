import requests
from bs4 import BeautifulSoup



#url = "http://192.168.43.123/JAVASCRIPT/list.html" 

url = "http://localhost/Javascript1/list.html" 


response = requests.get(url)
response.encoding = "UTF-8"
#print("status code :", response.status_code)
#print("response :", response.text)


soup = BeautifulSoup(response.text,'lxml')

for p in soup.find_all("td"):
    print(p)