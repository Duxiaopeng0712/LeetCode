def select_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


if __name__ == '__main__':
    nums = [3, 1, 5, 6, 7, 2, 4, 8]
    print(select_sort(nums))
