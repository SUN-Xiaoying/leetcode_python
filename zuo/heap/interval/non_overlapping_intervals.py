# https://leetcode.com/problems/non-overlapping-intervals/description/
from typing import List
import heapq

class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:



s = Solution()
# 1
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
# 2
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
# 0
print(s.eraseOverlapIntervals([[1,2],[3,4]]))