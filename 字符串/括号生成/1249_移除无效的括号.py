class Solution:
    def minRemoveToMakeValid(s: str) -> str:
        left, right, res = 0, s.count(')'), ''
        for i in range(len(s)):
            if s[i] == '(':
                if right > 0:
                    res += s[i]
                    left += 1
                    right -= 1
            elif s[i] == ')':
                if left > 0:
                    res += s[i]
                    left -= 1
                else:
                    right -= 1
            else:
                res += s[i]
        return res

if __name__ == '__main__':
    s = "lee(t(c)o)de)"
    print(Solution.minRemoveToMakeValid(s))
