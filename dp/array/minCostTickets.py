# https://leetcode.com/problems/minimum-cost-for-tickets/description/
# Med
from typing import List
import sys

class Solution:
    # 7 ms Beats 40.60%
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1, 7, 30]
        n = len(days)
        dp = [sys.maxsize]* (n+1)
        dp[n] = 0
        # days[i...] 最小花费
        for i in range(n, -1, -1): # for(int i = n-1; i>= 0; i--)
            j = i
            for k in range(len(durations)):
                while j < n and days[j] < days[i] + durations[k]:
                    j+=1
                dp[i] = min(dp[i], dp[j]+costs[k])

        return dp[0]

    # dp[]: cache
    # 1 ms Beats 84.59%
    # O(N)
    def mincostTickets2_dp(self, days: List[int], costs: List[int]) -> int:
        durations = [1, 7, 30]
        n = len(days)
        dp = [-1]*n
        # days[i...] 最小花费
        def f(i: int, dp: List[int]) -> int:
            if  i== n:
                return 0
            if dp[i] != -1:
                return dp[i]
            ans = float('inf')
            for k in range(3):
                j = i
                while j < n and days[j] < days[i] + durations[k]:
                    j += 1
                ans = min(ans, costs[k] + f(j, dp))

            dp[i] =ans
            return ans

        return f(0, dp)

    # Time Limit Exceeded
    # [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99]
    def mincostTickets1_timeout(self, days: List[int], costs: List[int]) -> int:
        durations = [1, 7, 30]
        n = len(days)
        # days[i...] 最小花费
        def f(i:int) -> int:
            if i == n:
                return 0
            ans = float('inf')
            for k in range(3):
                j = i
                while j<n and days[j] < days[i]+durations[k]:
                    j+=1
                ans = min(ans, costs[k] + f(j))
            return ans

        return f(0)


# days = [1,4,6,7,8,20], costs = [2,7,15]
# 11
s = Solution()
print(s.mincostTickets([1,4,6,7,8,20], [2,7,15]))