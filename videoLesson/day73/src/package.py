# from .plugins.disk import DiskPlugin
# from .plugins.mem import MemPlugin
# from .plugins.nic import NicPlugin

from day73.conf import settings

def pack():
    # obj1 = DiskPlugin()
    # disk_info = obj1.execute()
    #
    # obj2 = DiskPlugin()
    # mem_info = obj2.execute()
    #
    # obj3 = DiskPlugin()
    # nic_info = obj3.execute()
    #
    # response = {
    #     'nic': nic_info,
    #     'mem':mem_info,
    #     'disk':disk_info
    #
    # }
    response = {}
    for k,v in settings.PLUGINS.items():
        #response[k] = v().execute()  #v是字符串类型，所以不能直接这样执行，用反射。
        import importlib
        m_path, classname = v.rsplit('.', maxsplit=1) #只根据第一个进行分割
        # m = importlib.import_module('src.plugins.disk')#写死了
        m = importlib.import_module(m_path)
        cls = getattr(m, 'DiskPlugin')  #去模块获取类
        from day73.src.plugins import disk
        # content = disk.DiskPlugin().execute()
        # content = cls().execute()
        response[k] = cls().execute()
    return response

#如果再要加一个主板信息呢？
#尽量不要改源码
#写配置文件
