# https://leetcode.com/problems/container-with-most-water/description/
from typing import List


class Solution:
    # 可能并不是我变强了，而是很多题已经是第二遍听了
    #62ms Beats 93.64%
    def maxArea(self, height: List[int]) -> int:
        result=0
        l,r=0, len(height)-1
        while l<r:
            if height[l] <= height[r]:
                result = max(result, height[l]*(r-l))
                l+=1
            else:
                result = max(result, height[r] * (r - l))
                r -= 1

        return result

s = Solution()
# 49
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
# 1
print(s.maxArea([1,1]))