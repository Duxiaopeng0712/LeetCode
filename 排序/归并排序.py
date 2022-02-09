def merge(nums, low, mid, high):
    temp = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= high:
        temp.append(nums[j])
        j += 1

    nums[low: high + 1] = temp

def merge_sort(nums, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(nums, low, mid)
        merge_sort(nums, mid + 1, high)
        merge(nums, low, mid, high)
    return nums
if __name__ == '__main__':
    nums = [3, 1, 5, 6, 7, 2, 4, 8]
    print(merge_sort(nums, 0, len(nums) - 1))
