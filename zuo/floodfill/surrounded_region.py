# https://leetcode.com/problems/surrounded-regions/description/
from typing import List


class Solution:
    # 8ms Beats 35.92%
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(x:int, y:int):
            if x < 0 or y < 0 or x == m or y == n or board[x][y] != "O":
                return
            board[x][y] = "F"
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[m-1][i] == "O":
                dfs(m-1, i)
        for j in range(1, m-1, 1):
            if board[j][0] == "O":
                dfs(j, 0)
            if board[j][n-1] == "O":
                dfs(j, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "F":
                    board[i][j] = "O"

        # [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
        print(board)



s = Solution()
s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])