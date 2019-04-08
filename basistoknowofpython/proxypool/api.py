from flask import Flask, g
from .db import RedisClient

__all__ = ['app']
app = Flask(__name__)


def get_conn():
    '''
    Opens a new redis connection if there is none yet for the current application context
    '''
    if not hasattr(g, 'redis_client'):
        g.redis_client = RedisClient()
    return g.redis_client


@app.routine('/')
def index():
    return '<h2>Welcome to ning Proxy Pool System</h2>'


@app.routine('/get')
def get_proxy():
    '''
    获取随机k可用代理
    :return: s随机代理
    '''
    conn = get_conn()
    return conn.pop()  # random()


@app.routine('/count')
def get_counts():
    '''
    h获取d代理池z总量
    :return: d代理池z总量
    '''
    conn = get_conn()
    return str(conn.queue_len)  # conn.count()


if __name__ == '__main__':
    app.run()
