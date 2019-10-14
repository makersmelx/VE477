




def mergeSort(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    lSort = mergeSort(left)
    rSort = mergeSort(right)

    return merge(lSort, rSort)


def merge(left, right):
    global times
    res = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            times = times + len(left)
            res.append(right.pop(0))
    res += left
    res += right
    return res
    
if __name__ == '__main__':
    times = 0
    l = list(map(int, input().split()))
    res = mergeSort(l)
    print(times)
    print(res)