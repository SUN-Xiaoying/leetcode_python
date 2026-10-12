# https://leetcode.com/problems/trapping-rain-water/description/
# Hard
from typing import List


class Solution:
    # 3ms Beats 97.42%
    def trap_leetcode(self, height: List[int]) -> int:
        # 谁小结算谁
        lmax, rmax = height[0], height[-1]
        l, r = 1, len(height)-2
        result = 0
        # l==r 也要考虑
        while l<=r:
            if lmax <= rmax:
                if  lmax > height[l]:
                    result += lmax - height[l]
                else:
                    lmax = height[l]
                l+=1
            else:
                if rmax > height[r]:
                    result += rmax - height[r]
                else:
                    rmax = height[r]
                r-=1

        return result

    # 19ms Beats 41.31%
    def trap_pointer(self, height: List[int]) -> int:
        # 谁小结算谁
        lmax, rmax = height[0], height[-1]
        l, r = 1, len(height)-2
        result = 0
        # l==r 也要考虑
        while l<=r:
            if lmax <= rmax:
                result += max(0, lmax - height[l])
                lmax = max(lmax, height[l])
                l+=1
            else:
                result += max(0, rmax - height[r])
                rmax = max(rmax, height[r])
                r-=1

        return result



    # 23ms Beats 34.04%
    # 不是最优解，额外空间
    def trap_queue(self, height: List[int]) -> int:
        size = len(height)
        left, right = [0]*size, [0]*size
        max_left, max_right = -1, -1
        for i, num in enumerate(height):
            max_left = max(max_left, num)
            max_right = max(max_right, height[-1-i])
            left[i] = max_left
            right[size-1-i] = max_right

        result = 0
        # 范围是【1，n-2】，左右两边界不可能有水
        for i, num in enumerate(height):
            result += max(0, min(left[i], right[i])-num)
        return result




s = Solution()
# 6
print(s.trap_leetcode([0,1,0,2,1,0,1,3,2,1,2,1]))

