# 只放置可执行文件
#
# from ..src import package
# data_dict = package.pack()

# from ..src.plugins import * #解释一遍全放入内存
# from ..src import plugins #导入这个文件夹(包，模块，类库)，默认加载init文件到内存
#
#
# plugins.pack()


from ..src.script import run

if __name__ == '__main__':
    run()



