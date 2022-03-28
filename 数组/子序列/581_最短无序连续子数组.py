from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        newNums = sorted(nums)

        left = 0
        right = len(nums) - 1

        while left < len(nums):
            if nums[left] != newNums[left]:
                break
            left += 1

        while right > left:
            if nums[right] != newNums[right]:
                break
            right -= 1

        return right - left + 1

