from typing import List


class Solution:
    def findMagicIndex(nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return i

        return -1

if __name__ == '__main__':
    nums =[1,1,1,]
    print(Solution.findMagicIndex(nums))
