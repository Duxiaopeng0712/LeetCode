def quickSort(nums, left, right):
    if left >= right:
        return nums
    pivot = nums[left]
    start = left
    end = right

    while left < right:
        if left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]

        if left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[right] = pivot
    quickSort(nums, start, left - 1)
    quickSort(nums, left + 1, end)

    return nums


if __name__ == '__main__':
    nums = [3, 1, 5, 6, 7, 2, 4, 8]
    print(quickSort(nums, 0, len(nums) - 1))
