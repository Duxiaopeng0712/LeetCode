from typing import List


class Solution:
    def plusOne(digits: List[int]) -> List[int]:
        right = len(digits) - 1
        res = ''
        while right >= 0:
            if digits[right] != 9:
                digits[right] = digits[right] + 1
                break
            else:
                digits[right] = 0

            right -= 1
        if digits[0] == 0:
            digits.insert(0, 1)

        print(digits)
        return digits


if __name__ == '__main__':
    digits = [9, 9]

    Solution.plusOne(digits)
