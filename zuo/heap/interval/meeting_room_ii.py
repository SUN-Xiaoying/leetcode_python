# https://www.lintcode.com/problem/919/
# medium
import heapq
from typing import (
    List,
)

from heap.helper import Interval

class Solution:
    # 最大线段重合长度
    # Beat percent 96.9%
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        ans = 0
        minheap = []

        for interval in intervals:
            while minheap and minheap[0] <= interval.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, interval.end)
            ans = max(ans, len(minheap))

        return ans



s = Solution()
print(s.min_meeting_rooms([Interval(0, 30), Interval(5,10), Interval(15,20)]))