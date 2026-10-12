# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
from typing import List


class NumMatrix:
    # 118 ms Beats 50.42%
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix_sum = []
            return
        row = len(matrix)
        col = len(matrix[0])
        self.prefix_sum = [[0]*col for _ in range(row)]
        temp = 0
        # 要单独讨论行和列
        for i in range(row):
            temp += matrix[i][0]
            self.prefix_sum[i][0] = temp
        temp = 0
        for j in range(col):
            temp+= matrix[0][j]
            self.prefix_sum[0][j] = temp

        for i in range(1, row):
            for j in range(1, col):
                self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + self.prefix_sum[i][j-1] - self.prefix_sum[i-1][j-1] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # return self.prefix_sum[row2][col2] - self.prefix_sum[row1-1][col2] - self.prefix_sum[row2][col1-1] + self.prefix_sum[row1-1][col1-1]
        ps = self.prefix_sum
        total = ps[row2][col2]
        if row1 > 0:
            total -= ps[row1 - 1][col2]
        if col1 > 0:
            total -= ps[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            total += ps[row1 - 1][col1 - 1]
        return total

# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
# 8
print(obj.sumRegion(2, 1, 4, 3))
# 12
print(obj.sumRegion(1, 2, 2, 4))