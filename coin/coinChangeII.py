# https://leetcode.com/problems/coin-change-ii/description/
# Med
# Youtube: https://www.youtube.com/watch?v=Mjy4hd2xgrs
class Solution:
    # 203 ms Beats 91.44%
    def change(self, amount: int, coins: list[int]) -> int:
        coins.sort()
        dp = [0] * (amount+1)
        dp[0]=1
        for coin in coins:
            for n in range(coin, amount+1):
                dp[n] += dp[n-coin]

        return dp[amount]

s = Solution()
# 4
print(s.change(5, [1,2,5]))
# 0
print(s.change(3, [2]))
# 1
print(s.change(0, [7]))