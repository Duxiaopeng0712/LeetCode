from typing import List


class Solution:
    def findLength(nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)

        dp = [[0] * (len1 + 1) for _ in range(len2 + 1)]
        res = 0
        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                if nums1[j - 1] == nums2[i - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])

        return res


if __name__ == '__main__':
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    Solution.findLength(nums1, nums2)
