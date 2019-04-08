#NoSQL not only sql 基于键值对，不需要经过SQL层的解析，数据之间没有耦合性，性能非常高
#键值存储数据库，Redis, Voldemort OracleBDB
#列存储数据库，Cassandra,HBase, Riak
#文档型数据库，Couchdb,MongoDB
#图形数据库，Neo4J,InfoGrid,Infinite Graph

#对于爬虫数据来说，一条数据可能存在某些字段提取失败而缺失的情况，而且数据可能随时进行调整
#另外数据之间还存在嵌套关系，如果关系型 需要提前建表需要序列化操作 不方便。
#使用NoSQL 简单高效



import pymongo
#连接mongodb
client = pymongo.MongoClient(host='localhost', port=27017)
#MongoDB的连接字符串
#client = pymongo.MongoClient('mongodb://localhost:27017/')

#指定数据库
db = client.test
#db = client['test']

#指定集合，mongodb中每个数据库包含许多集合，类似于关系型数据库中的表
collection = db.students
#collection = db['students']

#插入数据
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
result = collection.insert(student)
print(result)

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170102',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
#result = collection.insert([student1, student2])
#print(result)

#官方推荐使用insert_one() insert_many()
student = {
    'id': '20170103',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert_one(student)
print(result)   #<pymongo.results.InsertOneResult object 对象
print(result.inserted_id)

#用列表形式传递给insert_many()

student1 = {
    'id': '20170101',
    'name': 'Jordansss',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170102',
    'name': 'Mikesss',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)



#查询，用find_one()查到的是单个结果，find()返回一个生成器对象
result = collection.find_one({'id':'20170101'})
print(type(result))
print(result)

#也可以根据ObjectId来查询
from bson.objectid import ObjectId
result = collection.find_one({'_id': ObjectId('5c723e40797518741c50a3a3')})
print(result)


#查询多条数据
results = collection.find({'age': 20}) #cursor类型，相当于一个生成器，需要遍历来取到所有结果，其中每个结果都是字典类型
print(results)
for r in results:
    print(r)

#查询的条件是字典，{'age': {'$in': [20, 23]}}
results = collection.find({'age': {'$gt': 20}})
print(results)

#以M开头的正则表达式
#$regrex $exists $type $mod  $text  {'$text':{'$search':'Mike'}} $where
results = collection.find({'name': {'$regex': '^M.*'}})

#计数
count = collection.find().count()
print(count)

#排序
#pymongo.ASCENDING指定升序  DESCENDING指定降序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])


#偏移
#偏移2个就忽略前两个元素，得到第三个及以后的元素
#limit指定要取的结果个数
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])


#数据量非常大的时候，不要使用大的便宜了查询数据，因为很可能导致内存溢出。采用如下
collection.find({'_id':{'$gt':ObjectId('5c72504779751875d95f927d')}})


#数据更新，指定更新条件和更新后的数据
condition = {'name':'Jordan'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)

#如果原先还有其他字段，不会更新也不会删除，只更新student内存在的字段
#result = collection.update(condition, {'$set': student})

#推荐使用update_one() update_many()
condition = {'name': 'Jordan'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)  #匹配的条数，影响的条数


condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

#删除
result = collection.remove({'name': 'Jordan'})
print(result)

#delete_one() delete_many()
#result.deleted_count获取删除的数据条数

#其他操作如 find_one_and_delete() find_one_and_replace() find_one_and_update()
#对索引进行操作 create_index() create_indexes() drop_index()








