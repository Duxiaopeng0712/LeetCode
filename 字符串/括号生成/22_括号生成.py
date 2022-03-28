from typing import List


class Solution:
    def generateParenthesis(n: int) -> List[str]:
        res = []
        def dfs(path, left,right):
            if left > n or left < right:
                return
            if len(path) == 2*n:
                res.append(path)
                return
            dfs(path + '(', left + 1, right)
            dfs(path + ')', left, right + 1)
        path = ''
        left = 0
        right = 0

        dfs(path, left, right)

        return res

if __name__ == '__main__':
    print(Solution.generateParenthesis(3))

