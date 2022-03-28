def maximumUniqueSubarray(nums):
    sum = 0
    start = 0
    end = 0
    max_sum = 0
    while end < len(nums):
        if end < len(nums) and nums[end] not in nums[start:end]:
            sum += nums[end]
            end += 1
            max_sum = max(max_sum, sum)
        else:
            start += 1
            end = start + 1
            sum = nums[start]
    return max_sum


if __name__ == '__main__':
    # nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    nums = [558, 508, 782, 32, 187, 103, 370, 607, 619, 267, 984, 10]
    # nums = [4,2,4,5,6]
    l = maximumUniqueSubarray(nums)
    print(l)
