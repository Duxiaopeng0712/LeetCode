from typing import List


class Solution:
    def searchRange(nums: List[int], target: int) -> List[int]:
        # def getIndex(nums, target):
        #     start, end = 0, len(nums)-1
        #     while start <= end:
        #         mid = (start + end) // 2
        #         if nums[mid] >= target:
        #             end = mid - 1
        #         else:
        #             start = mid + 1
        #     return start
        #
        # begin = getIndex(nums, target)
        # end = getIndex(nums, target + 1)
        # if begin==len(nums) or nums[begin] != target:
        #     return [-1, -1]
        # return [begin, end - 1]
        def findLeft(nums: List[int], target: int):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def findRight(nums: List[int], target: int):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        begin = findLeft(nums, target)
        end = findRight(nums, target)
        if begin == len(nums) or nums[begin] != target:
            return [-1, -1]
        return [begin, end]
if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution.searchRange(nums, target))
