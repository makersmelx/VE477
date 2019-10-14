import time


def knapsack_smallarr(nums, _sum):
    if _sum > sum(nums):
        return None
    # nums.sort()
    itr = 1
    while sum(nums[0:itr]) < _sum:
        itr = itr+1
    if sum(nums[0:itr]) > _sum:
        return None
    return nums[0:itr]


def knapsack(nums, _sum):
    # nums is sorted array
    if len(nums) == 1:
        if nums[0] == _sum:
            return [nums]
        else:
            return []
    if _sum == 0:
        if 0 in nums:
            return [[0]]
        return []
    res = []
    i = 0
    if nums[i] == _sum:
        res.append([nums[i]])
    elif nums[i] > _sum:
        return []
    else:
        target = _sum - nums[i]
        tmpList = [nums[i]]
        afterRes = knapsack(nums[i+1:], target)
        for i in range(len(afterRes)):
            afterRes[i] = tmpList + afterRes[i]

        res += afterRes
    return res


def sortRes(list):
    return list[0]


if __name__ == '__main__':
    _sum = int(input().strip())
    nums = list(map(int, input().strip().split()))
    # nums.sort()
    ticks = time.time()
    # res = knapsack(nums[1:], _sum - nums[0])
    # for i in range(len(res)):
    #     res[i] = [nums[0]]+res[i]

    res = knapsack_smallarr(nums, _sum)
    # print(res)
    print(time.time()-ticks)
