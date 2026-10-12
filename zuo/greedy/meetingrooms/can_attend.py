# https://www.lintcode.com/problem/920/
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        if len(intervals) < 2: return True
        intervals.sort(key = lambda x: x.start)
        last = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < last: return False
            last = interval.end
        return True

s = Solution()
# # False
# print(s.can_attend_meetings([(0,30),(5,10),(15,20)]))
# # True
# print(s.can_attend_meetings([(5,8),(8,15)]))
# True
print(s.can_attend_meetings([Interval(465,497),Interval(386,462),Interval(354,380),
                             Interval(134,189),Interval(199,282),Interval(18,104),
                             Interval(499,562),Interval(4,14),Interval(111,129),
                             Interval(292,345)]))