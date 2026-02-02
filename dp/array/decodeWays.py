# https://leetcode.com/problems/decode-ways/description/
# Med
from typing import List


class Solution:
    # 0 ms Beats 100.00%
    # 严格位置依赖
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n+1)
        dp[n] = 1
        for i in range(len(s)-1, -1, -1):
            if int(s[i]) == 0:
                dp[i]=0
                continue
            dp[i] = dp[i+1]
            if (i+1<n) and int(s[i:i+2])<= 26:
                dp[i] += dp[i+2]

        return dp[0]





    # 3 ms Beats 28.58%
    # dp
    def numDecodings_dp(self, s: str) -> int:
        def f(i:int, dp: List[int]) -> int:
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                dp[i] = 0
                return 0
            if dp[i] != -1:
                return dp[i]

            ans = f(i+1, dp)
            if i <len(s)-1 and (int(s[i])*10 + int(s[i+1])) <= 26:
                ans += f(i+2, dp)

            dp[i] = ans
            return ans

        return f(0, [-1]*len(s))

    # Time Limit Exceeded
    # 纯暴力递归
    def numDecodings_force(self, s: str) -> int:
        def f(i:int) -> int:
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            ans = f(i+1)
            if i <len(s)-1 and (int(s[i])*10 + int(s[i+1])) <= 26:
                ans += f(i+2)

            return ans

        return f(0)

s = Solution()
print(s.numDecodings("11106"))