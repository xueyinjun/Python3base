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
# count = collecton.find().count()
#统计符合某个条件的数据
# count = collection.find({'age':20}).count()
#排序调用sort()方法，并在其中传入排序的字段及升降序标志即可
# results = collection.find().sort('name',pymongo.ASCENDING)
# print(results['name']for result in results)
#偏移 利用skip()方法，偏移几个位置,还可以利用limit()方法指定要取的结果个数,在数据库数量庞大时，最好不要使用大的偏移量查询数据，很可能导致内存溢出
# results = collection.find()sort('name',pymongo.DESCENDING).skip(2).limit(2)
# print([results['name']for result in results])
#更新,使用update()方法，指定更新的条件和更新后的数据即可,返回的结果是字典型是，也可以使用$set操作符对数据进行更新
# condint ={'name':'Kevin'}
# student = collection.find_one(condint)
# student['age']=25
# result = collection.update(condint,student)
# print(result)
# result = collection.update(condint,{'$set':student})
#$set 这样可以只更新student字典内存在的字段，如果原先还有其他字段，则不会更新，也不会删除而如果不用$set的话，则会把之前的数据全部用student字典替换掉；如果原本存在其他字段，则会被删除
#推荐使用update_one()和update_many方法，它们的第二个参数需使用$类型操作符作为字典的键名,$inc 为加号
#删除 remove()方法指定删除条件即可，推荐方法 delete_one()和delete_many()
# result =collection.delete_one({'name':'Kevin'})
# print(result)
# print(result.delete_count)
# result =collection.delete_many({'age':{'$lt':25}})
# print(result..deleted_count)

#Redis存储，基于内存的高效的键值型菲关系数据库
# Redis 和StrictRedis,StrictRedis实现了绝大部分官方的命令，参数也是一一对应，而Redis是StrictRedis的子类，他的主要功能是用于向后兼容版本库里的几个办法，推荐使用StrictRedis
#连接Redis，首先声明StrictRedis对象，调用set()方法，设置一个键值对
# from redis import StrictRedis
# redis = StrictRedis(host='localhost',port=6379,db=0,password='von')
# redis.set('name','Bob')
# print(redis.get('name'))
#还可以用ConnectionPool连接，还支持通过URL来构建,直接将ConnectionPool当作参数传给StrictRedis
# from redis import StrictRedis,ConnectionPool
# pool = ConnectionPool(host='localhost',port=6379,db=0,password='von')
# redis = StrictRedis(connection_pool=pool)
#URL连接演示,连接字符串进行连接，调用from_url方法创建ConnectionPool，传递给StrictRedis
# url ='redis://:von@localhost:6370/0'
# pool = ConnectionPool.from_url(url)
# redis =StrictRedis(connetion_pool=pool)
#键操作:exists(name)判断一个键是否存在,keys(name)获取所有符合规则的键，move(name,db)将键移动到其他的数据库，delete(name)删除一个键
#字符串操作 set('name','Jordan'):给键赋值,get(name)返回键名为name的string的value,mset(mapping)批量赋值，mget(keys,*args)返回多个键对应的value
#列表操作：rpush(name,*values)在键为named的列表末尾添加值为value的元素，可以传多个,lpush(name,*values)在键为name的列表头添加值为value的元素，可以传多个，rpop(name)返回并删除键为name的，键名列表中的尾元素
#集合操作:sadd(name,*values)向键为name的集合中添加元素，srem(name,*values)从键为name的集合中删除元素,spop(name)s随机返回并删除键为name的集合中的一个元素，smove(src,dst,value):将src对应的集合中移除元素并将其添加到dst(目标集合)对应的集合中
#有序集合操作：zadd(name,*args,**kwargs)向键为name的zset中添加元素，memmber,score用于排序，zrem(name,*values)删除键为name的zset中的元素
#散列操作:hset(name,key,value)向键为name的散列中添加映射,hget(name,key)返回键为name的散列表中的key的对应值，hlen(name)从键为name的散列表中获取映射个数,hvals(name)散列表中获取所有映射键值，hgetall(namme)散列表中获取所有映射键值对
#RedisDump导入导出功能，redis-dump 用于导出数据，redis-load用于导入数据

