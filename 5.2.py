#关系型数据库存储 准备工作，2连接数据库，3创建表，4插入数据，5更新数据，6删除数据，7查询数据
#2连接数据库，PyMySQL的connect()方法声明一个MySQL连接对象db，此时要传入localhost基础配置,调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句，execute()写语句，fetchone()方法获得第一条数据
# import pymysql
# db = pymysql.connect(host='localhost', user='root', password='von', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

#3创建表
import pymysql

db = pymysql.connect(
    host='localhost', user='root', password='von', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255)NOT NULL, name VARCHAR(255)NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'
cursor.execute(sql)
db.close()
