
import time


def knapsack_arr(nums, _sum):
    if _sum > sum(nums):
        return None
    _storage = [[]]
    _storage += [None for i in range(_sum)]
    for i in range(len(nums)):
        tmp = []
        for j in range(_sum-nums[i]+1):
            if not _storage[j] is None and _storage[j+nums[i]] is None and not j in tmp:
                _storage[j+nums[i]] = _storage[j]+[nums[i]]
                tmp.append(j+nums[i])
            if not _storage[_sum] is None:
                return _storage[_sum]
    return _storage[_sum]


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
    for i in range(len(nums)):
        if nums[i] == _sum:
            res.append([nums[i]])
        elif nums[i] > _sum:
            break
        else:
            target = _sum - nums[i]
            tmpList = [nums[i]]
            afterRes = knapsack(nums[i + 1:], target)
            for i in range(len(afterRes)):
                afterRes[i] = tmpList + afterRes[i]

            res += afterRes
    return res


def sortRes(list):
    return list[0]


if __name__ == '__main__':
    import timeit

    _sum = int(input().strip())
    nums = list(map(int, input().strip().split()))
    # nums.sort()
    ticks = time.time()
    res = knapsack_arr(nums, _sum)
    # res = knapsack(nums, _sum)
    print(time.time()-ticks)
