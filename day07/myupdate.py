import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

 

# SQL문 실행
sql = "UPDATE mytable SET col2 = '123' WHERE col2 = '용진' "
curs.execute(sql)

 

# 데이타 Fetch
rows = curs.fetchall()

    # 전체 rows
for i in rows:
    print (i)



# Connection 닫기
conn.commit()
conn.close()