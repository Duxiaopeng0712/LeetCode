import math
from typing import List


class Solution:
    def findMin(nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]





if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    print(Solution.findMin(nums))
