# https://leetcode.com/problems/largest-1-bordered-square/
from typing import List


class Solution:
    # TODO: Best Solution
    # 1065 ms Beats 7.14%
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # 原地生成二维数组
        row = len(grid)
        col = len(grid[0])

        def get(i:int, j:int) -> int:
            return 0 if (i<0 or j<0) else grid[i][j]

        for i in range(row):
            for j in range(col):
                grid[i][j] += get(i-1, j) + get(i, j-1) - get(i-1, j-1)

        def get_sum(a:int, b:int, c:int, d:int)->int:
            # return (grid[c][d] + grid[a-1][d] + grid[c][b-1] - grid[a-1][b-1]) if c>=a else 0
            if a>c: return 0
            return get(c,d) - get(a-1,d) - get(c, b-1) + get(a-1, b-1)

        ans = 1
        for a in range(row):
            for b in range(col):
                c, d, k = a + ans, b + ans, ans + 1
                while c<row and d<col:
                    if (get_sum(a,b,c,d) - get_sum(a+1, b+1, c-1, d-1)) == (k-1)<<2: # why k*4 is not correct? It should be (k-1)*4
                        ans = k
                    c+=1
                    d+=1
                    k+=1

        return ans*ans

s = Solution()
#9
print(s.largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))
#0
print(s.largest1BorderedSquare([[0]]))

