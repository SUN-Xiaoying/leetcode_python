# https://leetcode.com/problems/number-of-islands/description/
from typing import List


class Solution:
    # 233ms Beats 84.69%
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        m = len(grid)
        n = len(grid[0])

        def dfs(x:int, y:int):
            if x<0 or y<0 or x==m or y==n or grid[x][y] != "1":
                return
            grid[x][y]=0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                    dfs(i,j)

        return count




s = Solution()
# 3
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))