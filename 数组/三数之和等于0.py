from typing import List


class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        lens = len(nums)
        if lens <= 0:
            return []
        for i in range(lens):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = lens - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while nums[left] == nums[left+1]:
                        left += 1
                    while nums[right] == nums[right-1]:
                        right -= 1
                    left, right = left + 1, right - 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        print(res)
        return res
if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    Solution.threeSum(nums)

