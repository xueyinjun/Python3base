#encoding = utf-8
#MongoDB存储
#我们使用PyMongo库里面的MongoClient,传入Mongo的IP及端口即可
import pymongo
client = pymongo.MongoClient(host='localhost',port=27017)
# host还可以传出MongoDB的连接字符串以mongodb为开头
# client=MongoClient('mongodb://localhost:27017/')
#指定数据库，需要指定操作哪个数据库,调用client的
db =client.test
#调用属性 方法是等价的
# db =client['test']
#指定集合:他们类似关系型数据库中的表
collection = db.students
# collection = db['students']
#插入数据：对象 调用insert()方法_id值，会在执行后返回,MongoDB中每条数据其实都是有一个_id属性来唯一标识的，如果没有显示指明该属性，MongoDB会自动产生一个ObjectID类型的_id属性,
# students ={
#     'id':'20170101',
#     'name':'Jordan',
#     'age':20,
#     'gender':'male'
# }
# students2 ={
#     'id':'20170202',
#     'name':'Mike',
#     'age':20,
#     'gender':'male'
# }
# result = collection.insert(students)
#同时插入多条数据，只需要以列表形式传递即可,
# result = collection.insert([students1,students2])
# print(result)
#推荐使用insert_one()方法，和insert_many()方法，插入单条和多条记录，insert_many我们可以将数据以列表形式传递，返回的数据也是列表形式
#查询：利用find_one()方法，或find()方法进行查询，find_one()查询得到的是单个结果，返回的结果是字典型，find()则返回一个生成器对象,返回结果是Curson类型需要遍历取得所有的结果
# result = collection.find_one({'name':'Mike'})
# print(type(result))
# print(result)
#我们可以根据ObjectId来查询，此时需要使用bson库里面的objectid
# from bson.objectid import ObjectId
# result = collection.find_one({'_id': ObjectId('5cb5841986560a04b266cf48')})
# print(result)
# results = collection.find({'age':20})
# print(results)
# for result in results:
#     print(result)
#比较符号
# results = collection.find({'name':{'$regex':'^M.*'}})
#统计用count()方法
count = collecton.find().count()
#统计符合某个条件的数据
count = collection.find({'age':20}).count()
#排序调用sort()方法，并在其中传入排序的字段及升降序标志即可
results = collection.find().sort('name',pymongo.ASCENDING)
print(results['name']for result in results)
#偏移 利用skip()方法，偏移几个位置,还可以利用limit()方法指定要取的结果个数,在数据库数量庞大时，最好不要使用大的偏移量查询数据，很可能导致内存溢出
results = collection.find()sort('name',pymongo.DESCENDING).skip(2).limit(2)
print([results['name']for result in results])
#更新,使用update()方法，指定更新的条件和更新后的数据即可,返回的结果是字典型是，也可以使用$set操作符对数据进行更新
condint ={'name':'Kevin'}
student = collection.find_one(condint)
student['age']=25
result = collection.update(condint,student)
print(result)
result = collection.update(condint,{'$set':student})
#$set 这样可以只更新student字典内存在的字段，如果原先还有其他字段，则不会更新，也不会删除而如果不用$set的话，则会把之前的数据全部用student字典替换掉；如果原本存在其他字段，则会被删除
#推荐使用update_one()和update_many方法，它们的第二个参数需使用$类型操作符作为字典的键名,$inc 为加号
#删除 remove()方法指定删除条件即可，推荐方法 delete_one()和delete_many()
result =collection.delete_one({'name':'Kevin'})
print(result)
print(result.delete_count)
result =collection.delete_many({'age':{'$lt':25}})
print(result..deleted_count)
