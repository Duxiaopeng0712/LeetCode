class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return check(low + 1, high) or check(low, high - 1)
        return True
