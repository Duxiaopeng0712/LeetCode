def Radix_sort(nums):
    if not nums: return []
    _max = max(nums)
    # 最大位数
    maxDigit = len(str(_max))
    bucketList = [[] for _ in range(10)]
    # 从低位开始排序
    div, mod = 1, 10
    for i in range(maxDigit):
        for num in nums:
            bucketList[num % mod // div].append(num)
        div *= 10
        mod *= 10
        idx = 0
        for j in range(10):
            for item in bucketList[j]:
                nums[idx] = item
                idx += 1
            bucketList[j] = []
    return nums

"""
找到数组最大值，得最大位数；
从最低位开始取每个位组成radix数组；
对radix进行计数排序（计数排序适用于小范围的特点）
"""
