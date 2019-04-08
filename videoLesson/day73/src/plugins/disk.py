from .base import BasePlugin
class DiskPlugin(BasePlugin):
    def linux(self):
        output = self.shell_cmd('ifconfig')
        # 正则表达式
        return output  #一般情况不直接返回
    def windows(self):
        output = self.shell_cmd('ipconfig')
        # 正则表达式
        return output