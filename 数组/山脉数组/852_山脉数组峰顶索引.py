from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ans = 0

        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                ans = i
                break

        return ans

