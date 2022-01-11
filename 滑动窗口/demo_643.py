import math


def findMaxAverage(nums, k):
    # 第一步：定义两个需要两个需要维护的变量
    sums, max_avg = 0, math.inf
    # 第二步：定义窗口的首尾端值
    start = 0
    for end in range(len(nums)):
        # 第三步：维护定义的变量：sums累加、max_avg求值
        sums += nums[end]
        if (end - start + 1 == k):
            max_avg = max(max_avg, sums / k)
        # 第四步：维护窗口：固定窗口（if）,窗口达到值，end后移，start也得保证后移以保证窗口数恒定
        if (end >= k - 1):
            sums -= nums[start]
            start += 1
    # 第五步：输出值
    return max_avg


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    res = findMaxAverage(nums, k)
    print(res)
