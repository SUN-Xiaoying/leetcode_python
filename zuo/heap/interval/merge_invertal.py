# https://leetcode.com/problems/merge-intervals/description/
# Easy
import heapq
from typing import List


class Solution:
    # 7 ms Beats 72.97%
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key= lambda x : x[0])
        cur = intervals[0]
        for interval in intervals:
            if cur[0] <= interval[0] <= cur[1]:
                cur[1] = max(interval[1],cur[1])
            else:
                result.append(cur)
                cur = interval
        result.append(cur)
        return result




s = Solution()
# [[1,6],[8,10],[15,18]]
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
# [[1,5]]
print(s.merge([[1,4],[4,5]]))
# [[1,7]]
print(s.merge([[4,7],[1,4]]))
