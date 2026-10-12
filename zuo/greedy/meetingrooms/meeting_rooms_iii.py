# https://www.lintcode.com/problem/1897/

from typing import (
    List,
)
import heapq
import bisect
class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """

    """
    room availability only matters at query start times, 
    heapq.pop() are already reflected when we record at the next start time
    """

    def meeting_room_i_i_i_timeout(self, intervals, rooms, ask):
        result = []

        for s, e in ask:
            heap = []
            for a, b in sorted(intervals):
                if b <= s or a >= e:
                    continue

                while heap and heap[0] <= a:
                    heapq.heappop(heap)

                heapq.heappush(heap, b)
                if len(heap) >= rooms:
                    result.append(False)
                    break
            else:
                result.append(True)

        return result

    def meeting_room_i_i_i(self, intervals, rooms, ask):
        # 1. Build difference map
        diff = {}
        for s, e in intervals:
            diff[s] += 1
            diff[e] -= 1

        # 2. Build hash map of active rooms at each time
        times = sorted(diff.keys())
        hm = {}
        active = 0
        for t in times:
            active += diff[t]
            hm[t] = active

        keys = times
        result = []

        # 3. Answer queries
        for s, e in ask:
            # find first index >= s
            i = bisect.bisect_left(keys, s)

            # rooms in use at time s
            if i == 0:
                current = 0
            else:
                current = hm[keys[i - 1]]

            ok = True

            # check all change points in [s, e)
            j = i
            while j < len(keys) and keys[j] < e:
                if hm[keys[j]] >= rooms:
                    ok = False
                    break
                j += 1

            # also check usage exactly at s
            if current >= rooms:
                ok = False

            result.append(ok)

        return result

    def meeting_room_i_i_i_mine(self, intervals: List[List[int]], rooms: int, ask: List[List[int]]) -> List[bool]:
        intervals.sort(key=lambda x: x[0])
        ask.sort(key=lambda x: x[0])

        min_heap = []
        result = []
        hm = {}

        for start, end in intervals:
            # free rooms
            while min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

            # record current room usage at this start time
            hm[start] = len(min_heap)

        keys = sorted(hm.keys())

        for s, e in ask:
            # find latest time <= s
            i = bisect.bisect_right(keys, s)
            if i == 0:
                used = 0
            else:
                used = hm[keys[i - 1]]

            result.append(used < rooms)

        return result

s = Solution()
# [false,true]
print(s.meeting_room_i_i_i([[1,2],[4,5],[8,10]],1,[[4,5],[5,6]]))

# [true,true]
print(s.meeting_room_i_i_i([[1,2],[4,5],[8,10]],1,[[2,3],[3,4]]))