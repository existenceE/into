import pymysql

# db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version: ', data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4')
# db.close()


# db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db = 'spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) not null, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close


# id = '20120001'
# user = 'Bob'
# age = 20

db = pymysql.connect(host = 'localhost', user='root', password='12345678', port=3306, db='spiders')
cursor = db.cursor()
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# #事务的原子性，发生或没有发生。如插入一条数据要么全部插入要么都不插入不存在插入一般的情况。
# #ACID ，还有一致性 隔离性，互不干扰 持久性，改变是永久性的其他操作不应该对其有任何影响
# #标准写法
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()  #增删改都需要用commit才能生效
# except:
#     db.rollback()  #相当于什么都没发生过
# db.close()

#实现动态构造 用字典和元组 进行改写
#
# data = {
#     'id': '20120003',
#     'name': 'Charles',
#     'age': 30
# }
# table = 'students'
#
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,values=values) #如果主见已经存在 执行更新操作
# update = ','.join([" {key} = %s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values())*2):  #('20120002', 'Amy', 21, '20120002', 'Amy', 21)
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#删除操作
# table = 'students'
# condition = 'age > 20'
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

#查询数据

# sql = 'SELECT * FROM students WHERE age >= 20'
#
# try:
#     cursor.execute(sql)
#     print('Count:', cursor.rowcount) #rowcount同济个数
#     one = cursor.fetchone()
#     print('One:', one)
#     results = cursor.fetchall() #剩下的
#     print('Results:', results)
#     print('Results Type:', type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')


#如果数据量很大，占用开销会非常高。采用逐条取数据while + fetchone()替代fetchall()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')






















