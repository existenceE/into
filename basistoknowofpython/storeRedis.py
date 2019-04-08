#redis-py库提供两个类 Redis StrictRedis来实现Redis的命令操作

from redis import StrictRedis, ConnectionPool


redis = StrictRedis(host='localhost', port=6379, db=0, password='')
redis.set('name', 'Bob')
print(redis.get('name'))

pool = ConnectionPool(host='localhost', port=6379, db=0, password='')
redis = StrictRedis(connection_pool=pool)

#ConnectionPool还支持通过URL来构建，URL的格式支持有几种
#redis://[:password]@host:port/db    redis TCP
#rediss://[:password]@host:port/db   redis TCP+SSL
#unix://[:password]@/path/to/socket.sock?db=db  redis UNIX socket

url = 'redis://:@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
print(redis.get('name'))

# 键操作
# redis.exists('name')
# redis.delete('name')
# redis.type('name')
# redis.keys('n*')
# randomkey()
# redis.rename('name', 'nickname')
# dbsize()
# redis.expire('name', 2)
# redis.ttl('name')  获取键的国企时间
# move('name', 2)
# flushdb()
# flushall()

#字符串操作
# redis.set('name', 'Bob')
# redis.get('name')
# redis.getset('name', 'Mike'))
# redis.mget(['name', 'nickname'])
# redis.setnx('newname', 'James')
# redis.setex('name', 1, 'James')
# redis.set('name', 'Hello')
# redis.setrange('name', 6, 'World')
# redis.mset({'name1': 'Durant', 'name2':'James'})
# redis.msetnx({'name3': 'Smith', 'name4':'Curry'})
# redis.incr('age', 1)
# redis.decr('age', 1)
# redis.append('nickname', 'OK')
# redis.substr('name', 1, 4)
# redis.getrange('name', 1, 4)

#列表操作，列表内的元素可以重复，而且可以从两端存储
# redis.rpush('list', 1, 2, 3) 结果为3，列表大小
# redis.lpush('list', 0) 结果为4
# redis.llen('list') 返回长度 4
# redis.lrange('list', 1, 3) [b'3', b'2', b'1']
# redis.ltrim('list', 1, 3) True
# redis.lindex('list', 1)
# redis.lset('list', 1, 5) 索引为1的位置赋值5
# redis.lrem('list',2, 3) 删除两个3
# redis.lpop('list') 返回并删除第一个元素
# redis.rpush('list') 返回并删除最后一个元素
# redis.blpop('list') 返回并删除第一个元素，可以设置超时，如果列表为空，一直等待
# redis.brpop('list') 可以设置超时
# redis.rpoplpush('list', 'list2') 返回并删除src的微元素并添加到list2的头部


# 集合操作 redis提供集合存储，集合中的元素都是不重复的
# redis.sadd('tags', 'Book', 'Tea', 'Coffee') 向键为tags的集合中后面三个元素 返回3，即插入数据个数
# redis.srem('tags', 'Book') 从键为tags的集合中删除Book,1为删除的数据个数
# redis.spop('tags') 随机删除并返回该元素
# redis.smove('tags', 'tags2', 'Coffee')  返回True
# redis.scard('tags') 获取集合中元素的个数
# redis.sismember('tags', 'Book') 判断Book是否为tags的集合元素
# redis.sinter(['tags', 'tags2']) 返回键为tags的集合和键为tags2的集合的交集
# redis.sinterstore('inttag', ['tags', 'tags2']) 求键为tags和tags2的集合的交集并将其保存为inttag
# redis.sunion(['tags', 'tags2']) 返回并集
# redis.sunionstore('inttag', ['tags', 'tags2']) 3
# redis.sdiff(['tags', 'tags2']) 返回差集
# redis.sdiffstore('inttag', ['tags', 'tags2']) 3
# redis.smembers('tags') 返回键为tags的集合的所有元素
# redis.srandmember('tags') 随机返回tags中的一个元素

# 有序集合操作，比集合多了一个分数字段，可以对其排序
# redis.zadd('grade',100,'Bob',98, 'Mike')  返回2，即为添加的元素个数
# redis.zrem('grade', 'Mike') 从键为grade的zset中删除Mike，即删除的元素个数1
# redis.zincrby('grade', 'Bob', -2)
# redis.zrange('grade', 'Amy')
# redis.zrevrank('grade', 'Amy') 获取倒数排名
# redis.zrevrange('grade', 0, 3) 返回键为grade的zset中前四名元素
# redis.zrangebyscore('grade', 80, 95) 返回键为grade的zset中score在80和95之间的元素
# redis.zcount('grade', 80, 95) 之间的元素个数
# redis.zcard('grade') 获取键为grade的zset中元素个数
# redis.zremrangebyrank('grade', 0, 0) 删除排名第一的元素，返回1 即为删除的元素个数
# redis.zremrangebyscore('grade', 80, 90) 删除之间的元素

# 散列操作
# redis.hset('price', 'cake', 5)
# redis.hsetnx('price', 'cake', 6) 如果不存在则添加映射
# redis.hget('price', 'cake') 获取键为price的散列表中键名为cake的值
# redis.hmget('price', ['apple', 'orange']) 获取两个的值
# redis.hmset('price', {'banana':2, 'pear':6}) 向键为price的散列表中批量添加映射
# redis.hincrby('price', 'apple', 3) 为apple的值增加3
# redis.hexists('price', 'banana')
# redis.hdel('price', 'banana')
# redis.hlen('price')
# redis.hkeys('price') 获取所有映射键名
# redis.hvals('price')
# redis.hgetall('price') 获取所有键值对



# redis-dump用于导出数据，redis-load用于导入数据



# redis-dump -u :foobared@localhost:6379 -f adsl:* > . /redis .data.jl
# < redis_data.json redis-load -u :foobared@localhost:6379
# cat redis_data.jso「i I redis-load -u :foobared@localhost:6379

#后面会利用redis实现很多架构，如维护代理池，cookies池，adsl拨号代理池，scrapy-redis分布式架构等等，
























