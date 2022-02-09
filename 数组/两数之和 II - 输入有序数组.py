from typing import List


class Solution:
    def twoSum(numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
        return [-1, -1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    Solution.twoSum(numbers, target)
