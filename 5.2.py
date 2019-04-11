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
# import pymysql

# db = pymysql.connect(
#     host='localhost', user='root', password='von', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255)NOT NULL, name VARCHAR(255)NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'
# cursor.execute(sql)
# db.close()

#4插入数据,Value直接用格式化来实现，execute()方法的第一个参数传入该SQL语句，Value值用统一的元组传过来
#db对象的commit方法才可实现数据插入，这个方法才是真正将语句提交到数据库执行的方法，异常处理调用rollback()执行数据回滚

# import pymysql
# id = '20120001'
# user = 'Bob'
# age = 20

# db = pymysql.connect(
#     host='localhost', user='root', password='von', port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id,name,age) value(%s,%s,%s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

#插入、更新和删除操作都是对数据库操作进行更改的操作，而更改操作都必须为一个事务，所以标准写法，这样便可以保证数据的一致性，这里的commit()和rollback()方法就为事务的实现提供了支持
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

#插入通用方法动态变化的字典,
#传入的数据是字典，并将其定义为data变量，表名也定义成变量table，,构造插入的字段，需要构造多个占位符，定义长度为1的[%s]的数组，然后用乘法扩充，再利用字符串的format()方法将表名字段名和占位符构造出来
# import pymysql
# db = pymysql.connect(
#     host='localhost', user='root', password='von', port=3306, db='spiders')
# cursor = db.cursor()
# data = {'id': '20120001', 'name': 'Bob', 'age': 20}
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) value({values})'.format(
#     table=table, keys=keys, values=values)
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Fauled')
#     db.rollback()

#更新数据,如果我们传入的id仍为20,但是年龄变化从20变为21 注意mysql顺序
# import pymysql
# db = pymysql.connect(
#     host='localhost', user='root', password='von', port=3306, db='spiders')
# cursor = db.cursor()
# data = {'id': '20120001', 'name': 'Bob', 'age': 21}

# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))

# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(
#     table=table, keys=keys, values=values)
# update = ','.join([" {key} = %s".format(key=key) for key in data]) # 更新语句，主键存在
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#删除数据  因为删除条件多种多样运算符有大于，小于，等于，LIKE等，条件连接符有AND、OR等，所以这里将条件当做字符串传递，已实现删除操作
# import pymysql
# db = pymysql.connect(
#     host='localhost', user='root', password='von', port=3306, db='spiders')
# cursor = db.cursor()
# data = {'id': '20120001', 'name': 'Bob', 'age': 21}
# table = 'students'
# condition = 'age>20'
# sql = 'DELETE FROM {table} where {condition}'.format(
#     table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

#查询数据 不用commit()方法，用cursor的rowcount属性获取查询结果的条数，fetchone()方法获取结果的第一条数据，返回结果是元组形式，调用fetchall()方法可以得到结果的所有数据，它是二重元组，fetchone()和fetchall()fetchone指针向下移
# import pymysql
# db = pymysql.connect(
#     host='localhost', user='root', password='von', port=3306, db='spiders')
# cursor = db.cursor()
#
# sql ='SELECT *FROM students WHERE age>=20'
# try:
#     cursor.execute(sql)
#     print('Count',cursor.rowcount)
#     one = cursor.fetchone()
#     print('One:',one)
#     results = cursor.fetchall()
#     print('Results:',results)
#     print('Results Type:',type(results))
#     for row in results:
#         print(row)
# except:
#     print('Eorr')

#while + fetchone()获取所有数据，fetcall()会将结果以元组形式全部返回，如果数据量大，会占用开销非常高，推荐逐条取数据
# sql = 'SELECT *FROM students WHERE age>=20'
# try:
#     cursor.execute(sql)
#     print('Count:', cursor.rowcount)
#     row = cursor.fetchone()
#     while row:
#         print('ROW:', row)
#         row = cursor.fetchone()
# except:
#     print('Eorror')
