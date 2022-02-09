from typing import List

"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""


class Solution:
    def permuteUnique(nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                # 判断是否使用重复数字
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(nums, path, res, used)
                path.pop(len(path) - 1)
                used[i] = False
        # 1、排序：去重的基础
        nums.sort()
        path = []
        res = []
        used = [False] * len(nums)
        dfs(nums, path, res, used)
        return res

if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution.permuteUnique(nums))
