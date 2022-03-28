class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:

            mid = (left + right) // 2
            if arr[left] == target:
                return left
            elif arr[mid] == target:
                right = mid
            elif arr[right] == target:
                left = mid + 1
            elif arr[mid] < arr[right]:
                if arr[mid] < target < arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif arr[mid] > arr[right]:
                if arr[left] < target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1
        return -1

"""
末尾元素一定小于等于首位元素（假设数组长度大于1）
由两个单调数组组成，且后面的数组不大于前面的数组。
查找算法时间复杂度上限为O(n)，但是旋转数组是否可以通过二分查找解决呢，答案是：可以。
折半思路对于折半查找来说，我们通过中间元素的值arr[mid]和target比较，从而决策出下一次查找的区间是左还是右区间，同样，对于旋转数组，我们也按照这样的思路来计算。所以我们应该如何设置判断条件，从而决定下一次的决策区间是左边还是右边呢？
回顾一下，单调数组如何进行折半查找，判断条件是什么。如果一个数组单调掉递增的话，我们做如下判断：
    while left <= right:
    如果arr[mid] == target 返回mid
    如果arr[mid] < target，说明target在左半区间，因此在左半区间查找
    否则，在右半区间查找
    结束条件left>right 返回-1
    那么对于旋转数组我们也按照同样的思想，就是通过判断target在那个半区间，从而在相应的区间继续查找。我们做如下判断：
    if arr[left] == target return left 优先返回左边元素
    elif arr[mid] == target right = mid 左半区间（包含右端点）一定存在目标元素，所以找左半区间
    elif arr[right] == target left = mid + 1 右半区间（不包含右端点）一定存在目标元素，且左半区间一定不存在目标元素，通过条件1和条件2可以得出。
    elif arr[mid] < arr[right] 说明右区间是单调的，因此可以通过右半区间端点判断target是不是属于右区间，如果在右区间，则left = mid + 1，否则，right = mid - 1
    elif aarr[mid] > arr[right] 说明左半区间是单调的，同样可以通过左半区间的端点判断target是不是属于左半区间，如果属于则 right = mid - 1,否则，left = mid + 1
    else 说明arr[mid] = arr[right] 这时候就稍微复杂点了，因为无法左右到底哪部分是单调的，可是后通过暴力缩减区间，即right-1。
"""
