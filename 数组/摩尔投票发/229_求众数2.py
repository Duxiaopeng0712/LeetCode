from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp_dict = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in temp_dict:
                temp_dict[nums[i]] += 1
            else:
                temp_dict[nums[i]] = 1

        for j in temp_dict:
            if temp_dict[j] > (len(nums) // 3):
                res.append(j)

        return res
