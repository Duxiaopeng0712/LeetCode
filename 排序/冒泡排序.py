def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


if __name__ == '__main__':
    nums = [3, 1, 5, 6, 7, 2, 4, 8]
    print(bubble_sort(nums))
