# https://leetcode.com/problems/fibonacci-number/
# Easy
from typing import List


class Solution:
    # 有限变量
    # 35 ms Beats 84.57%
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        lastlast, last = 0, 1

        for i in range(2, n+1):
            cur = lastlast + last
            lastlast = last
            last = cur

        return last

    # memorize dp: f(i) -> f(i, dp)
    # 43 ms Beats 55.44%
    def fib2(self, n: int) -> int:

        dp = [-1] * (n + 1)
        return self.f2(n, dp)

    def f2(self, n: int, dp: List[int]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if dp[n] != -1:
            return dp[n]

        dp[n] = self.f2(n - 1, dp) + self.f2(n - 2, dp)

        return dp[n]


    # 从底到顶
    # 44 ms Beats 51.97%
    # O(N)
    def fib3(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    # 347 ms Beats 18.25%
    # The slowest O(2^n)
    def fib1_dumbest(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib_dumbest(n-1) + self.fib_dumbest(n-2)

s = Solution()
# 13
print(s.fib(7))
# 21
print(s.fib(8))

