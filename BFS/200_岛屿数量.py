from typing import List
class Solution:
    def numIslands(grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        def dfs(i, j):
            grid[i][j] = '0'
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                row_i = i + x
                col_j = j + y

                if 0 <= row_i < row and 0 <= col_j < col and grid[row_i][col_j] == '1':
                    dfs(row_i, col_j)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res
if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(Solution.numIslands(grid))

