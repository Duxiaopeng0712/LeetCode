class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                temp = stack.pop()
                stack[-1] += max(2*temp, 1)

        return stack.pop()
