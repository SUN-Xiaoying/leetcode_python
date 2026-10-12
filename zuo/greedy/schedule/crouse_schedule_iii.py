# https://leetcode.com/problems/course-schedule-iii/description/
from typing import List
import heapq # minheap

class Solution:
    # 53 ms Beats 40.42%
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        sum = 0
        max_heap = []
        courses.sort(key=lambda x: (x[1]))
        for duration, timeline in courses:
            sum += duration
            # java MaxHeap
            # PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b)->b)
            heapq.heappush(max_heap, -duration)

            if sum > timeline:
                sum += heapq.heappop(max_heap)

        return len(max_heap)

s = Solution()
# 3
print(s.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]))
# 0
print(s.scheduleCourse([[3,2],[4,3]]))
# 5
print(s.scheduleCourse([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]))