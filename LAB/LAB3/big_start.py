import time


def knapsack_bigarr(nums, _sum):
    if (_sum > sum(nums)):
        return None
    nums.sort()
    i = len(nums)-1
    tmp = 0
    result = []
    while tmp < _sum and i >= 0:
        if tmp+nums[i] <= _sum:
            result.append(nums[i])
            tmp += nums[i]
        i -= 1
    if tmp != _sum:
        return None
    return result


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
            afterRes[i] += tmpList

        res += afterRes
    return res


def sortRes(list):
    return list[0]


if __name__ == '__main__':
    _sum = int(input().strip())
    nums = list(map(int, input().strip().split()))
    # nums.sort(reverse=True)

    ticks = time.time()
    # res = knapsack(nums[1:], _sum - nums[0])
    # for i in range(len(res)):
    #     res[i] += [nums[0]]
    res = knapsack_bigarr(nums, _sum)
    # print(res)
    print(time.time()-ticks)
