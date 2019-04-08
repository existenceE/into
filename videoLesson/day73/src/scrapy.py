# 采集资产并且用三种不同的形式
# 优势：扩展容易 比如可以增加memPlugin.不用关心当前模式，只用告诉命令就行。

from ..conf import settings
# class BasePlugin:
#     def __init__(self):
#         mode_list = ['SSH', 'Salt', 'Agent']
#         if settings.MODE in mode_list:
#             self.mode = settings.MODE
#         else:
#             raise Exception('配置文件错误')
#
#     def ssh(self, cmd):
#         pass
#
#     def agent(self,cmd):
#         pass
#     def salt(self, cmd):
#         pass
#
#     def shell_cmd(self, cmd):
#         if self.mode == 'SSH':
#             ret = self.ssh(cmd)
#         elif self.mode == 'Salt':
#             ret = self.salt(cmd)
#         else:
#             ret = self.agent(cmd)
#         return ret
#
#     def execute(self):
#
#
#         # settings.MODE  #用户可能填错 可能没填
#         # 判断平台
#         # agent模式
#         # import subprocess
#         # subprocess.getoutput('..')
#
#         # ssh
#         ####
#
#         # saltstack
#         # if self.mode == 'SSH':
#         #     ret = self.ssh('判断平台')
#         # elif self.mode == 'Salt':
#         #     ret = self.salt('判断平台')
#         # else:
#         #     ret = self.agent('判断平台')
#         ret = self.shell_cmd('查看平台命令')
#         if ret == 'win':
#             self.windows()
#         elif ret == 'linux':
#             self.liunx()
#         else:
#             raise Exception('ONLY SUPPORT WINDOWS AND LINUX.')
#
#     def linux(self):
#         raise Exception('.....')
#
#     def windows(self):
#         raise Exception('...')


# obj = BasePlugin()
# obj.execute()

# 不用BasePlugin
class DiskPlugin(BasePlugin):
    def linux(self):
        output = self.shell_cmd('ifconfig')
        # 正则表达式
        return output  #一般情况不直接返回
    def windows(self):
        output = self.shell_cmd('ipconfig')
        # 正则表达式
        return output

class MemPlugin(BasePlugin):
    pass




obj = DiskPlugin()  #说明配置文件是对的
result = obj.execute()  #采集机器硬盘信息
