# https://leetcode.com/problems/house-robber/description/
from typing import List


class Solution:
    # 压缩空间啊
    # 0ms Beats 100.00%
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        prepre = nums[0]
        pre = max(nums[0], nums[1])
        ans = pre

        for i in range(2, len(nums)):
            cur = max(pre, nums[i]+prepre)
            ans = max(cur, ans)
            prepre = pre
            pre = cur

        return ans

    # 0 ms Beats 100.00%
    def rob_dp(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 2:
            return max(nums)

        dp=[0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n, 1):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[-1]

s = Solution()
# 12
print(s.rob([2,7,9,3,1]))
# 1
print(s.rob([1,1]))
# 4
print(s.rob([2,1,1,2]))
# 3
print(s.rob([1,3,1]))