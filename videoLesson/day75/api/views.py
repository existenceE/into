from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.
import hashlib
import time


ck = '12123dsda'
auth_lst = []
@csrf_exempt
def asset(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    # print(request.body, type(request.body))  #bytes类型
    auth_key_time = request.META['HTTP_AUTHKEY']
    auth_key_client, client_ctime = auth_key_time.split('|')

    server_current_time = time.time()
    if server_current_time-30 > float(client_ctime): #太久远 时间节点上过滤掉一批请求 推30秒
        return HttpResponse('授权失败')
    if auth_key_time in auth_lst:
        return HttpResponse('你来晚了')
    auth_lst.append(auth_key_time)

    #用户的Key可能不对
    key_time = "%s|%s" %(ck, client_ctime,)
    m = hashlib.md5()
    m.update(bytes(key_time, encoding='utf-8'))
    authkey = m.hexdigest()



    if auth_key_client != authkey:
        return HttpResponse('鉴权失败')
    if request.method == 'POST':  #只有POST的body里面才有数据
        import json
        host_info = json.loads(str(request.body,encoding='utf-8'))
        print(host_info)
    return HttpResponse('...')


def test(request):
    response = render(request, 'index.html')
    response.set_signed_cookie('kkk','vvv')  #签名的cookie
    return response