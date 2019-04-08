# #
# # def orderedSequentialSearch(alist, item):
# #     pos = 0
# #     found = False
# #     stop = False
# #     while pos < len(alist) and not found and not stop:
# #         if alist[]
# #
# #
# #
# #
# #
# #
# #
# # testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# # print(orderedSequentialSearch(testlist, 3))
# # print(orderedSequentialSearch(testlist, 13))
#
#
# #无序列表顺序搜索
# def sequentialSearch(alist, item):
#     found = False
#     pos = 0
#     while pos < len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# #有序列表顺序搜索
# def orderedSequentialSearch(alist, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         elif alist[pos] > item:
#             stop = True
#         else:
#             pos += 1
#     return found
#
#
# # #二分搜索法 更好利用有序的优势
# # def binarySearch(alist, item):
# #     first = 0
# #     last = len(alist) - 1
# #    # mid = len(alist) // 2  #double / inappropriate position and caculate ways
# #     found = False
# #     while first < last and not found:
# #         mid = (first + last) // 2
# #         if alist[mid] == item:
# #             found = True
# #         elif alist[mid] < item:
# #             #binarySearch(alist[mid+1:last], item)
# #             first = mid + 1
# #         else:
# #             #binarySearch(alist[first: mid], item)
# #             last = mid - 1
# #     return found
#
#
# # log(n)
#
# def binarySearch(alist, item):
#     first = 0
#     last = len(alist) - 1
#     found = False
#     while first <= last and not found:
#         mid = (first + last) // 2
#         if item == alist[mid]:
#             found = True
#         elif item < alist[mid]:
#             last = mid - 1
#         else:
#             first = mid + 1
#     return found
#
#
# #递归版本 需要重复训练
# def recurBinarySearch(alist, item):
#     if len(alist) == 0:
#         return False
#     else:
#         mid = len(alist) // 2
#         if alist[mid] == item:
#             return True
#         elif item < alist[mid]:
#             return recurBinarySearch(alist[:mid], item)
#         else:
#             return recurBinarySearch(alist[mid+1:], item)
#
#
# print(recurBinarySearch([1,2,3,4,5,6,7,8,9], 8))
#
#
#
# def hash(astring, tablesize):
#     sum = 0
#     for pos in range(len(astring)):
#         sum += ord(astring[pos])
#     return sum % tablesize


# #冒泡 两个for，一个for是比较的次数，第二个for是一次的具体比较
# def bubbleSort(alist):
#     for p in range(len(alist)-1, 0, -1):
#         for i in range(p):
#             if alist[i] > alist[i+1]:
#                 alist[i], alist[i+1] = alist[i+1], alist[i]
# alist = [56,26,93,17,77,31,44,55,20]
# alist = []
# bubbleSort(alist)
# print(alist)
#
# #改良冒泡。如果一次排序过程中没有交换，就可以断定已经排好，因此可以改良冒泡，使其在已知列表排好的情况下提前结束
#
# def shortBubbleSort(alist):
#     exchanges = True
#     p = len(alist) - 1
#     while p > 0 and exchanges:
#         exchanges = False
#         for i in range(p):
#             if alist[i] > alist[i+1]:
#                 alist[i], alist[i+1] = alist[i+1], alist[i]
#                 exchanges = True
#             p -= 1




#选择排序
# def selectionSort(alist):
#     for f in range(len(alist)-1, 0, -1):
#         maxPosi = 0
#         for i in range(1, f+1):
#             if alist[maxPosi] < alist[i]:
#                 maxPosi = i
#         alist[maxPosi], alist[f] = alist[f], alist[maxPosi]
#
# alist = [56,26,93,17,77,31,44,55,20]
# selectionSort(alist)
# print(alist)

#插入排序
# def insertionSort(alist):
#     sortedPos = 0
#     for i in range(sortedPos+1, len(alist)):
#         if alist[i] < alist[sortedPos]:
#             alist[i], alist[sortedPos] = alist[sortedPos], alist[i]
#         sortedPos += 1


# def insertionSort(alist):
#     for index in range(1, len(alist)):
#         currentvalue = alist[index]
#         pos = index
#         while pos > 0 and alist[pos-1] > currentvalue:
#             alist[pos] = alist[pos-1]
#             pos -= 1
#             alist[pos] = currentvalue


#
# def insertionSort(alist):
#     for index in range(1, len(alist)):
#         pos = index
#         currentvalue = alist[index]
#         while pos > 0 and alist[pos-1] > currentvalue:
#             alist[pos] = alist[pos-1]
#             pos -= 1
#             alist[pos] = currentvalue

#希尔排序

#归并排序


# class Foo(type):
#     def __new__(cls, name, bases, attrs):
#         print("cls: ", cls)
#         print("name: ", name)
#         print("bases: ", bases)
#         print("attrs: ", attrs)
#         return type.__new__(cls, name, bases, attrs)
#
# class A():
#     pass
# class B():
#     pass
# class FooChild(B, A, metaclass=Foo):
#     pass
# class FooChild2(B, A):
#     __metaclass__=Foo
#
# print(FooChild())
# print(FooChild2())





















