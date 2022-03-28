import math


def minSubArrayLen(nums, target):
    start = 0
    sums = 0
    min_len = math.inf

    for end in range(len(nums)):
        sums += nums[end]
        while sums >= target:
            min_len = min(min_len, end - start + 1)
            sums -= nums[start]
            start += 1
    if min_len == math.inf:
        return 0
    return min_len


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    l = minSubArrayLen(nums, 7)
    print(l)
