import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums, max_sum = 0, nums[0]

        for start in nums:
            sums = max(sums + start, start)
            max_sum = max(max_sum, sums)
        return max_sum

