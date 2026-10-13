# https://leetcode.com/problems/sliding-window-maximum/description/
# Hard
# Zuo: https://www.bilibili.com/list/8888480?sid=3509640&oid=618407664&bvid=BV11h4y1w7Bu 单调队列？

from collections import deque

class Solution:
    # 211 ms Beats 25.13%
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        result = []
        for index, value in enumerate(nums):
            while queue and value >= nums[queue[-1]]:
                queue.pop()
            queue.append(index)
            if index >= k-1:
                result.append(nums[queue[0]])
            while queue and index - queue[0] >= k-1:
                queue.popleft()
        return result


s = Solution()
# [3,3,5,5,6,7]
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# [1,-1]
print(s.maxSlidingWindow([1,-1], 1))