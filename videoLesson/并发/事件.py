

from multiprocessing import Event


e = Event()
print(e.is_set())

# print('1111111')
# e.wait()
#
# print('22222222')
# e.wait()

e.set()

print('333333')
print(e.is_set())
e.wait()

print('444444')
e.clear()
print(e.is_set())
e.wait()

print(e.is_set())
