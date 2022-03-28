from typing import List


class Solution:
    def combine(n: int, k: int) -> List[List[int]]:
        def dfs(path, res, index):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(index, n+1):
                path.append(i)
                dfs(path, res, i + 1)
                path.pop()
        path = []
        res = []
        dfs(path, res, 1)
        return res


if __name__ == '__main__':
    print(Solution.combine(4,2))
