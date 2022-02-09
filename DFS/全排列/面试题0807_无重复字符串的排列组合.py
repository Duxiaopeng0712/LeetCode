from typing import List

"""
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。
"""


class Solution:
    def permutation(S: str) -> List[str]:
        def dfs(S, path, res):
            if len(path) == len(S):
                res.append(path)
                return

            for i in range(len(S)):
                if S[i] in path:
                    continue
                path = path + S[i]
                dfs(S, path, res)
                path = path[:-1]

        path = ''
        res = []
        dfs(S, path, res)
        return res


if __name__ == '__main__':
    S = "qwe"
    print(Solution.permutation(S))
