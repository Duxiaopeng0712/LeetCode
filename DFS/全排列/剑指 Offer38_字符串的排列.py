from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(s, path, res, used):
            if len(path) == len(s):
                res.append(path)
                return

            for i in range(len(s)):
                if used[i]:
                    continue
                if used[i] or (i > 0 and s[i] == s[i - 1] and not used[i - 1]):
                    continue
                path = path + s[i]
                used[i] = True
                dfs(s, path, res, used)
                path = path[:-1]
                used[i] = False

        temp = sorted(list(s))
        path = ''
        res = []
        used = [False] * len(temp)
        dfs(temp, path, res, used)
        return res
