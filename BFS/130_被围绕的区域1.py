from typing import List


class Solution:
    def solve(board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return board
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = 'B'
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                row_i = i + x
                col_j = j + y
                if 1 <= row_i < row and 1 <= col_j < col and board[row_i][col_j] == 'O':
                    dfs(row_i, col_j)
        # 遍历行
        for i in range(col):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[row - 1][i] == 'O':
                dfs(row - 1, i)
        # 遍历列
        for j in range(row):
            if board[j][0] == 'O':
                dfs(j, 0)
            if board[j][col - 1] == 'O':
                dfs(j, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'
        return board
if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    res = Solution.solve(board)
    print(res)
