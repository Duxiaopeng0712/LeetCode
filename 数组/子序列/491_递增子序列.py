from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(start_index, path):
            # 终止条件
            if len(path) >= 2:
                if path[-1] >= path[-2]:
                    result.append(path)
                else:
                    return
                    # 回溯
            for i in range(start_index, len(nums)):
                # 去重
                if nums[i] in nums[start_index:i]:
                    continue
                backtracking(i + 1, path + [nums[i]])

        backtracking(0, [])
        return result


