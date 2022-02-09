from typing import List


class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
        res = 0
        i = 0
        if nums[-1] < target:
            nums.append(target)
            res = len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                res = i
                break
        print(res)
        return res


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    Solution.searchInsert(nums, target)
