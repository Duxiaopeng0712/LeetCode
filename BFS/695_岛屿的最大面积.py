from typing import List


class Solution:
    def maxAreaOfIsland(grid: List[List[int]]) -> int:
        row, col, res = len(grid), len(grid[0]), 0

        def dfs(i, j):
            grid[i][j] = 0
            temp = 1
            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                row_i = i + x
                col_j = j + y
                if 0 <= row_i < row and 0 <= col_j < col and grid[row_i][col_j] == 1:
                    temp += dfs(row_i, col_j)

            return temp

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res

if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    print(Solution.maxAreaOfIsland(grid))
