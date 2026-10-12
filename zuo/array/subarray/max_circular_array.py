# https://leetcode.com/problems/maximum-sum-circular-subarray/
from typing import List


class Solution:
    # 28 ms Beats 97.74%
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        all_sum = 0 # if keep all_sum = nums[0]
        # incorrectly misses the case where the entire array is the max subarray
        min_pre, max_pre = 0, 0
        min_sum, max_sum = nums[0], nums[0]

        for i in range(len(nums)):
            min_pre += nums[i]
            max_pre += nums[i]
            all_sum += nums[i]
            if min_pre < min_sum: min_sum = min_pre
            if max_pre > max_sum: max_sum = max_pre
            if max_pre < 0: max_pre = 0
            if min_pre > 0: min_pre = 0

        if all_sum == min_sum: return max_sum
        return max(all_sum - min_sum, max_sum)

    # 107 ms Beats 26.87%
    # 环形数组最大累加和，
    # 1. 不连续数组最大累加和
    # 2. 掐头去尾最小累加和
    def maxSubarraySumCircular_from_one(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)
        max_sum, min_sum = float('-inf'), float('inf')
        max_pre, min_pre = nums[0], nums[0]
        all_sum = nums[0]

        for i in range(1,len(nums)):
            max_pre = max(nums[i], nums[i]+max_pre)
            max_sum = max(max_sum, max_pre)

            min_pre = min(nums[i], nums[i]+min_pre) # 可以省去一次比较
            min_sum = min(min_sum, min_pre)

            #             max_curr += num
            #             min_curr += num
            #             if max_curr > max_total:
            #                 max_total = max_curr
            #             if min_curr < min_total:
            #                 min_total = min_curr
            #             if max_curr < 0:
            #                 max_curr = 0
            #             if min_curr > 0:
            #                 min_curr = 0

            all_sum+=nums[i]

        if all_sum == min_sum: return max_sum

        return max(max_sum, all_sum-min_sum)




    # 见环形就拷贝
    def maxSubarraySumCircular_copy(self, nums: List[int]) -> int:
        n = len(nums)
        # if n <= 2: return max(nums)
        # dp = [0] * n
        # ans = float('-inf')

        nums2 = nums * 2  # simulate circular array
        dp = [0] * (2 * n)
        ans = float('-inf')

        for i in range(0,n*2):
            # i = i%n
            # dp[i] = max(nums2[i], nums2[i]+dp[i-1], nums2[i]+dp[(i+1)%n])
            if i == 0:
                dp[i] = nums2[i]
            else:
                dp[i] = max(nums2[i], nums2[i] + dp[i - 1])

            # # only consider subarrays of length ≤ n
            if i >= n:
                dp[i - n] = 0  # reset old influence (can't exceed n length)

            ans = max(dp[i], ans)

        return ans

s = Solution()
# -2
print(s.maxSubarraySumCircular([-2]))
# -1
print(s.maxSubarraySumCircular([-2, -1]))
# 3
print(s.maxSubarraySumCircular([1,-2,3,-2]))
# 10
print(s.maxSubarraySumCircular([5,-3,5]))