from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == target:
                count += 1
            else:
                if count >= 1:
                    count -= 1
                else:
                    target = nums[i]

        return target
