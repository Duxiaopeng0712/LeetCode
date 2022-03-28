# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, nums: 'nums') -> int:
        N = nums.length()
        peek = self.findPeek(target, nums)
        left_index = self.findInAscOrder(target, nums, 0, peek)
        right_index = self.findInDecOrder(target, nums, peek, N - 1)
        if left_index != -1:
            return left_index
        else:
            return right_index

    def findPeek(self, target, nums):
        N = nums.length()
        left, right = 1, N - 2
        while left <= right:
            mid = left + (right - left) // 2
            if nums.get(mid - 1) < nums.get(mid) > nums.get(mid + 1):
                return mid
            elif nums.get(mid - 1) < nums.get(mid) < nums.get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findInAscOrder(self, target, nums, begin, end):
        left, right = begin, end
        while left <= right:
            mid = left + (right - left) // 2
            print(left, right, mid)
            cur = nums.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def findInDecOrder(self, target, nums, begin, end):
        left, right = begin, end
        while left <= right:
            mid = left + (right - left) // 2
            cur = nums.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

"""
    提示1. 山脉数组的左右两部分分别有序
提示2. array数组总长度是 10000，总的读取元素的次数不超过 100 次。
根据这两点，我们可以 100% 地确定用二分查找方法。

题目的难点在于找到 target 出现的第一个位置，如果我们想着只在山峰的左边或者右边使用一次二分查找的话，没法确定一次就就查找到。因此必须在山峰的左右两边都进行二分查找。

那么思路就是：

找到山峰的位置
在山峰的左边查找 target
如果查找不到，则在山峰的右边查找 target

"""
