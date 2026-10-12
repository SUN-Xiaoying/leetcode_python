# https://www.lintcode.com/problem/919

from typing import (
    List,
)

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

import heapq

class Solution:
    # 81 ms, Your submission beats 96.40 % Submissions
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        min_heap = []
        result = 0
        for interval in intervals:
            while min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            result = max(result, len(min_heap))

        return result




s = Solution()
# 2
print(s.min_meeting_rooms([Interval(0,30),Interval(5,10),Interval(15,20)]))
# 1
print(s.min_meeting_rooms([Interval(0,8),Interval(8,10)]))
# 4
print(s.min_meeting_rooms([Interval(1,10),Interval(2,9),Interval(3,8),Interval(4,7)]))
# # 2
# print(s.min_meeting_rooms([(5,10),(0,30),(15,20)]))