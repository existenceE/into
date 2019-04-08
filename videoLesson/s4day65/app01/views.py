from django.shortcuts import render, redirect
import pymysql
import random


# 用户一访问classes 就把数据库所有班级列出来
def classes(request):
    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                           passwd='1qaz2wsx', db='videoLesson', charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, title from class")
    class_list = cursor.fetchall()
    print(class_list)
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return render(request, 'classes.html', {"classlist": class_list})


def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')
    else:
        print(request.POST)
        v = request.POST.get('title')  # 取得前台name的key value
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                               passwd='1qaz2wsx', db='videoLesson',
                               charset='utf8')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into class(id, title) values(%s, %s)",
                       [random.randint(1, 100), v, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return redirect('/classes/')


def del_class(request):
    nid = request.GET.get('nid')

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                           passwd='1qaz2wsx', db='videoLesson',
                           charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id=%s", [nid, ])
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return redirect('/classes/')  # 重定向就是立即再发一次请求


def edit_class(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                               passwd='1qaz2wsx', db='videoLesson',
                               charset='utf8')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id=%s", [nid, ])
        result = cursor.fetchone()
        print(result)
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return render(request, 'edit_class.html', {'result': result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                               passwd='1qaz2wsx', db='videoLesson',
                               charset='utf8')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id=%s", [title, nid, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return redirect('/classes/')
