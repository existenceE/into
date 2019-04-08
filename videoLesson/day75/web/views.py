from django.shortcuts import render,HttpResponse
import json

# Create your views here.


from django.views import View


class AssetView(View):
    def get(self, request, *args, **kwargs):
        #从数据库获取数据，通过模板引擎渲染
        #这次全都基于ajax.看到裸页面
        return render(request, 'asset.html')


class AssetJsonView(View):
    def get(self, request, *args, **kwargs):
        #从数据库获取数据
        table_config = [
            {
                'q':'id',
                'title':'ID',
                'display':False,
                'text':{}
            },
            {
                'q': 'cabinet_num',
                'title': '机柜号',
                'display': True,
                'text': {'content':"{n}-{m}", 'kwargs':{'n':'机柜', 'm':'xxx'}} #字符串格式化把n编程机柜

            },
            # "123-{n}.html".format({'n':'alex'})


            {
                'q': 'cabinet_order',
                'title': '机柜位置',
                'display': True,
                'text': {'content': "{n}-{m}",
                         'kwargs': {'n': '机柜', 'm': 'xxx'}}  # 字符串格式化把n编程机柜

            },
        ]
        q_list = []
        for i in table_config:
            if not i['q']:
                continue
            q_list.append(i['q'])

        from repository import models
        data_list = models.Asset.objects.all().values(*q_list) #QuerySet类型，不能直接dumps，要先list  #id 和 name列
        data_list = list(data_list)
        print(data_list)
        result = {
            'table_config':table_config,
            'data_list':data_list,
        }
        return HttpResponse(json.dumps(result))
        # return render(request, 'asset.html',
        #               {
        #                   'table_config':table_config,
        #               })





