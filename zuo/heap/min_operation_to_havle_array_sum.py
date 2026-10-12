# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
# Medium
from typing import List
import heapq

class Solution:
    # TODO: Not the best way
    # 270 ms Beats 29.34%
    def halveArray(self, nums: List[int]) -> int:
        sum = 0
        maxheap = []

        for num in nums:
            sum += num
            heapq.heappush(maxheap, -num)

        sum /= 2
        times = 0

        while sum > 0:
            diff = -(heapq.heappop(maxheap) / 2) # What if diff > sum? >>> at least half.
            sum -= diff
            times+=1
            heapq.heappush(maxheap, -diff)

        return times

s = Solution()
# 3
print(s.halveArray([5,19,8,1]))
# 3
print(s.halveArray([3,8,20]))