from typing import List


class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        slow, fast = 0, 0
        nums_len = len(nums)
        while fast != nums_len:
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


if __name__ == '__main__':
    nums = [1, 1, 1, 2]
    print(Solution.removeDuplicates(nums))
