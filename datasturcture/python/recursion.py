
# def text(n):
#     if n > 0:
#         print("抱着", end="")
#         text(n-1)
#         print("的我", end="")
#     else:
#         print("我的小鲤鱼", end="")
# text(5)


# n楼梯，可以走一层，也可以走两层
# 按照最后一步，走一层的方法+走两层的方法
# f(1)=1 f(2)=2
# f(n) = f(n-1) + f(n-2)


# 汉诺塔 移动n个圆盘 只能小圆盘放在大圆盘上面
# 移动n个圆盘 = 移动n-1个 + 移动第n个
# A初始柱子 B经过的柱子 C 要到的柱子


def hanoi(n, A, B, C):
    if n > 0:
        # n个盘子从A经过B移动到C
        hanoi(n-1, A, C, B)
        # hanoi(1, A, None, C)
        print("%s->%s" %(A, C))
        hanoi(n-1, B, A, C)

hanoi(2, "A", "B", "C")
# def hanoi(n):
#     if n >= 1:
#         hanoi(n-1)
#         print("moving %s" % n)
#     else:
#         print("done")
#
# hanoi(5)