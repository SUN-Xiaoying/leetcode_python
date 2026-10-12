# https://leetcode.com/problems/couples-holding-hands/description/
from typing import List


class Solution:
    # 0ms Beats 100.00%
    def minSwapsCouples(self, row: List[int]) -> int:

        n = len(row) // 2
        count = n
        father = list(range(n))

        def find(i: int) -> int:
            if i != father[i]:
                father[i] = find(father[i])
            return father[i]

        def union(x, y):
            nonlocal count
            fx = find(x)
            fy = find(y)
            if fx != fy:
                father[fx] = fy
                count -= 1

        for i in range(0, len(row), 2):
            union(row[i] // 2, row[i + 1] // 2)
        return len(father) - count

    # 1ms Beats 16.61%
    def minSwapsCouples_Zuo(self, row: List[int]) -> int:
        father = []
        count = 0

        def build(m:int):
            nonlocal count
            for i in range(0, m, 1):
                father.append(i)
            count = m

        def find(i: int) -> int:
            if i!= father[i]:
                father[i] = find(father[i])
            return father[i]

        def union(x, y):
            nonlocal count
            fx = find(x)
            fy = find(y)
            if fx != fy:
                father[fx] = fy
                count -= 1

        n = len(row)
        build(n//2)
        for i in range(0, n, 2):
            union(row[i]//2, row[i+1]//2)
        return n//2 - count






s = Solution()
print(s.minSwapsCouples([0,2,1,3]))