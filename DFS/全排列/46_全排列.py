"""
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列
"""
from typing import List


class Solution:
    def permute(nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(nums, path, res)
                path.pop(len(path) - 1)

        path = []
        res = []
        dfs(nums, path, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution.permute(nums))
