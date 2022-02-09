from typing import List


class Solution:
    def search(nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] == nums[start]:
                start += 1
                continue
            # 前半部分有序
            if nums[mid] > nums[start]:
                # 前半部分查找
                if nums[start] <= target and nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            # 后半部分查找
            else:
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution.search(nums, target))
