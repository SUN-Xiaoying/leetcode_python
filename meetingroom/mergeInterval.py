# https://leetcode.com/problems/merge-intervals/description/
# Med
import heapq

class Solution:
    # 11 ms Beats 26.34%
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        heap = []
        result = []
        head, tail = intervals[0]
        heapq.heappush(heap,intervals[0][1])
        for interval in intervals:
            if heap and interval[0] <= heap[0]:
                head = min(head, interval[0])
            if interval[0] > tail:
                result.append([head, tail])
                while heap and interval[0] > heap[0]:
                    heapq.heappop(heap)
                head = interval[0]
            tail = max(tail, interval[1])
            heapq.heappush(heap, interval[1])

        result.append([head, tail])
        return result

s = Solution()
# [[1,6],[8,10],[15,18]]
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))