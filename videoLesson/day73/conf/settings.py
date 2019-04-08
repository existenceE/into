
MODE = 'Agent' #Salt,SSH

PLUGINS = {
    'disk': 'src.plugins.disk.DiskPlugin',  #完全根据配置文件有谁执行谁
    'mem': 'src.plugins.mem.MemPlugin',
    'nic': 'src.plugins.nic.NicPlugin',
}