def insert_sort(nums):
    for i in range(len(nums)):
        while i > 0 and nums[i-1] > nums[i]:
            nums[i], nums[i-1] = nums[i - 1], nums[i]
            i -= 1

    return nums


if __name__ == '__main__':
    nums = [3, 1, 5, 6, 7, 2, 4, 8]
    print(insert_sort(nums))
