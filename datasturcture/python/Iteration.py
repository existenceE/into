
def list_sum(num_list):
    sum = 0
    for i in num_list:
        sum += i
    return sum
print (list_sum([1,3,5,7,9]))


#numlist[0] + numlist[1:]
#不用while或for循环
#可以看做是列表中第一个元素和剩下所有元素之和

def list_sum2(num_list):
    if len(num_list) == 1:  #边界条件 基本结束条件 规模小到可以直接被解决的问题
        return num_list[0]
    return num_list[0] + list_sum2(num_list[1:])  #改变自己的状态并向基本结束条件演进

print(list_sum2([1,3,5,7,9]))



# def to_str(n, base):
#     convert_string = "0123456789ABCDEF"
#     if n < base:
#         return convert_string[n]
#     else:
#         return to_str(n / base, base) + convert_string[n % base]
#
# print(to_str(16, 16))

#
# import Stack
# r_stack = Stack()
# def to_str(n, base):
#     convert_string = "0123456789ABCDEF"
#     while n > 0:
#         if n < base:
#             r_stack.push()
#















