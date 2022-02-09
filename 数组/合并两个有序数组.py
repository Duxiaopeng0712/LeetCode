from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1  # 目标数组总长度
        while m > 0 and n > 0:  # 只要两个数组任意一个遍历完
            if nums1[m - 1] > nums2[n - 1]:  # 一数组最后一个比二最后一个大
                nums1[k] = nums1[m - 1]  # 将一数组最后一个移到目标数组最后一个
                m -= 1  # 一数组的指针左移
            else:
                nums1[k] = nums2[n - 1]  # 将二数组最后一个移到目标数组最后一个
                n -= 1  # 将二数组的指针左移
            k -= 1  # 目标数组指针左移
        nums1[:n] = nums2[:n]  # 如果第二个数组未遍历完，说明一数组已排序好，将二数组剪切过来

