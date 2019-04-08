





def f(x, l=[]):
    print(id(l))
    for i in range(x):
        l.append(i*i)
    print(l)


f(3)
f(2)