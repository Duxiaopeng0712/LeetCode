class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else :
                high = high - 1
        return nums[low]
"""
首先，创建两个指针 leftleft, rightright 分别指向 numbersnumbers 首尾数字，然后计算出两指针之间的中间索引值 middlemiddle，然后我们会遇到以下三种情况：

middlemiddle > rightright ：代表最小值一定在 middlemiddle 右侧，所以 leftleft 移到 middle + 1middle+1 的位置。
middlemiddle < rightright ：代表最小值一定在 middlemiddle 左侧或者就是 middlemiddle，所以 rightright 移到 middlemiddle 的位置。
middlemiddle 既不大于 leftleft 指针的值，也不小于 rightright 指针的值，代表着 middlemiddle 可能等于 leftleft 指针的值，或者 rightright 指针的值，我们这时候只能让 rightright 指针递减，来一个一个找最小值了。
"""
