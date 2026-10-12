# https://leetcode.com/problems/maximum-subarray/description/
from typing import List


class Solution:
    # Compress space
    # 92ms Beats 25.59%
    def maxSubArray_pre(self, nums: List[int]) -> int:
        pre, ans = nums[0], nums[0]
        for i in range(1, len(nums), 1):
            pre = max(nums[i]+pre, nums[i])
            ans = max(pre, ans)

        return ans

    # 112ms Beats 6.12%
    def maxSubArray_dp(self, nums: List[int]) -> int:
        n = len(nums)
        # 创建dp数组
        dp = [0]*n
        dp[0] = nums[0]
        ans =  nums[0]
        for i in range(1,n,1):
            dp[i] =nums[i] + max( dp[i-1], 0)
            ans = max(ans, dp[i])

        return ans

    def maxSubArray(self, nums: List[int]) -> tuple[int, int, int]:
        pre, ans = nums[0], nums[0]
        l, r = 0, 0

        for i in range(1, len(nums), 1):

            if pre >= 0:
                pre += nums[i]
            else:
                l=r
                pre = nums[i]

            if ans < pre:
                r=i
                ans = pre

        return l, r, ans


s = Solution()
# 3, 6, 6
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
#0, 4, 23
print(s.maxSubArray([5,4,-1,7,8]))