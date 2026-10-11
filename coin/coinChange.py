# https://leetcode.com/problems/coin-change/description/
# Med
# Youtube: https://www.youtube.com/watch?v=H9bfqozjoqs

class Solution:
    # Bottom up
    # 451ms Beats 82.06%
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        dp = [amount+1]*(amount + 1)
        dp[0] = 0
        for a in range(1, amount+1):
            for coin in coins:
                if a >= coin:
                    dp[a] = min(dp[a], 1 + dp[a-coin])
        return dp[amount] if dp[amount] != amount+1 else -1


    # Greedy does not work
    def coinChange_greedy(self, coins: list[int], amount: int) -> int:
        total_num = 0
        current_num = 0
        total_amount = 0
        coins.sort()
        # an infinite number of each kind of coin.
        for coin in reversed(coins):
            if coin > amount:
                continue
            current_num = amount // coin
            total_num +=  current_num
            current_amount = coin * current_num
            amount -= current_amount

        if amount > 0:
            return -1

        return total_num








s = Solution()
# 3
# print((s.coinChange([1,2,5], 11)))
# 3
# print((s.coinChange([1,3,5], 9)))
# 20
print(s.coinChange([186,419,83,408], 6249))