

import redis


conn = redis.Redis(host='127.0.0.1', port=6379, password="")

v = conn.keys()
print(v )


print(conn.smembers("dupefilter:xiaodongbei"))