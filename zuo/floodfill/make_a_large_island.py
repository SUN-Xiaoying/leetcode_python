# https://leetcode.com/problems/making-a-large-island/description/
from typing import List


class Solution:
    # 609ms Beats 86.92%
    def largestIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        index = 2

        # 1. dfs
        def dfs(x:int, y:int, index:int) -> int:
            if x<0 or y<0 or x==m or y==n or grid[x][y] != 1:
                return 0
            grid[x][y]=index
            area = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                area += dfs(x + dr, y + dc, index)
            return area
            # dfs(x-1, y)
            # dfs(x+1, y)
            # dfs(x, y-1)
            # dfs(x, y+1)

        # 2. Change id
        # 3. Calculate size
        sizes = {}
        sizes[0] = 0
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[index] = dfs(i, j, index)
                    result = max(result, sizes[index])
                    index+=1

        # 4. Discuss "0"
            # visited = set(), and id not in visited
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    up = grid[i-1][j] if i>0 else 0
                    down = grid[i+1][j] if i<m-1 else 0
                    left = grid[i][j-1] if j>0 else 0
                    right = grid[i][j+1] if j<n-1 else 0
                    merge = 1
                    visited.add(up)
                    merge += sizes[up]

                    if down not in visited:
                        merge += sizes[down]
                        visited.add(down)

                    if left not in visited:
                        merge += sizes[left]
                        visited.add(left)

                    if right not in visited:
                        merge += sizes[right]
                        visited.add(right)

                    result = max(result, merge)
                    visited.clear()

        return result




s = Solution()
# 25
print(s.largestIsland([
    [1,1,0,0,1,1,1,0],
    [1,1,0,0,1,1,1,0],
    [1,1,1,0,1,0,0,0],
    [0,0,0,1,1,0,0,0],
    [1,1,1,0,0,0,0,0],
    [1,1,0,0,1,0,0,0],
    [0,1,1,1,0,1,1,1],
    [0,0,0,0,1,0,0,0]
]))