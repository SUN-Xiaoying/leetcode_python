# https://leetcode.com/problems/number-of-islands/description/
from os import unlink
from typing import List


class Solution:
    # 250ms Beats 51.85%
    def numIslands_Zuo(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        father = [0]*m*n
        sets = 0

        # index
        def index(x:int, y:int)->int:
            return int(x*n) + y

        # build
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    idx = index(i, j)
                    father[idx] = idx
                    sets+=1
        # find
        def find(x:int) -> int:
            if father[x] != x:
                father[x] = find(father[x])
            return father[x]

        # union
        def union(a:int, b:int, c:int, d:int):
            nonlocal sets
            fx = find(index(a,b))
            fy = find(index(c,d))
            if fx!= fy:
                father[fx] = fy
                sets-=1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if i>0 and grid[i-1][j] == "1":
                        union(i, j, i-1, j)
                    if j>0 and grid[i][j-1] == "1":
                        union(i, j, i, j-1)

        return sets


s = Solution()
# 3
print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))