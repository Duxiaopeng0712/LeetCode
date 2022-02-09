from typing import List


class Solution:
    def removeElement(nums: List[int], val: int) -> int:
        index, move = 0, 0
        while move < len(nums):
            if nums[move] != val:
                nums[index] = nums[move]
                index += 1
            move += 1
        print(index)
        return index


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    Solution.removeElement(nums, val)
