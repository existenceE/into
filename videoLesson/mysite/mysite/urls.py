"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse, render, redirect


def login(request):
    """
    处理用户请求并返回内容
    :param request: 用户请求相关所有信息（对象
    :return:
    """
    # 值加字符串
    # HttpResponse单一的功能 只能传输字符串
    # 找到文件显示出来 用render
    # return HttpResponse('<input type="text" />')
    # 自动找到模板路径下的login.html，读取内容并返回给用户
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # 用POST提交的数据
        u = request.POST.get('username')
        p = request.POST.get('password')
        if u == 'root' and p == '123321':
            return redirect("/index/")
        else:
            return render(request, 'login.html', {"msg": "用户名或密码错误"})


def index(request):
    return render(
        request,
        'index.html',
        {
            'name': 'mxn',
            "users": ['lz', 'zz'],
            'user_dict': {'k1': 'v1', "k2": 'v2'},
            'user_list_dict': [
                {'id': 1, "name": 'alex', "email": 'alex@qq.com'},
                {'id': 2, "name": 'alex2', "email": 'alex2@qq.com'},
                {'id': 3, "name": 'alex3', "email": 'alex3@qq.com'},
            ]
        }
    )


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login),
    path('index/', index),
]
