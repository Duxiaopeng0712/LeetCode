from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return True
        # return False
        if len(nums) == 0:
            return False
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[start]:
                start += 1
                continue
            # 前半部分有序
            if nums[mid] > nums[start]:
                # 前半部分查找
                if nums[start] < target and nums[mid] >= target:
                    end = mid - 1
                # 后半部分查找
                else:
                    start = mid + 1
            # 后半部分有序
            else:
                # 后半部分查找
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                # 前半部分查找
                else:
                    end = mid - 1
        return False
