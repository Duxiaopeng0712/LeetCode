from typing import List


class Solution:
    def removeDuplicates(nums: List[int]) -> int:

        slow, fast = 0, 0

        while fast < len(nums):
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(slow)
        return slow

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    Solution.removeDuplicates(nums)

