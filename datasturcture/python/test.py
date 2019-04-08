


# 有循环减半 所以是O(logn)
def binarySearch(l, item):
    low = 0
    high = len(l)-1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if l[mid] == item:
            found = True
        elif l[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return found


li = list(range(1000))

print(binarySearch(li, 100 2))