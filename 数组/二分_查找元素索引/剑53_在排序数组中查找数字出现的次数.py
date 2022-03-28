from typing import List




# class Solution:
#     def search(nums: List[int], target: int) -> int:
#         start, end, count = 0, len(nums) - 1, 0
#         while start <= end:
#             mid = start + (end - start) // 2
#             if nums[mid] > target:
#                 end = mid - 1
#             elif nums[mid] < target:
#                 start = mid + 1
#             else:
#                 count += 1
#                 end = mid - 1
#         print(count)
#         return count
class Solution:
    def search(nums: List[int], target: int) -> int:
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

        return findRight(nums, target) - findLeft(nums, target) + 1


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution.search(nums, target))
