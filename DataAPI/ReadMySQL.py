# Python读取MySQL数据库数据
import pymysql

db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)

cur = db.cursor()
cur.execute('use world')
selectsql = '''select * from countrylanguage 
where Language = 'Chinese' and Percentage>10'''
cur.execute(selectsql)
data = cur.fetchall()

for item in data:
    print(item)
db.close()
