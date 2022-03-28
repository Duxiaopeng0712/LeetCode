from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2 or arr[0] >= arr[1]:
            return False

        temp = 1
        for i in range(2, len(arr)):
            if temp and arr[i-1] >= arr[i]:
                # 下山
                temp = 0
            if not temp and arr[i - 1] <= arr[i]:
                # 下山完又上山
                return False

        if temp == 1:
            # 一直上山
            return False
        else:
            return True
