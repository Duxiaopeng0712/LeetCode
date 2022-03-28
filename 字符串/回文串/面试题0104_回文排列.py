class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        temp = set()

        for i in range(len(s)):
            if s[i] in temp:
                temp.remove(s[i])
            else:
                temp.add(s[i])

        return len(temp) < 2
