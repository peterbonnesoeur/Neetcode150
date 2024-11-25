# To redo urgently

# We fill the different possibilities from the biggest to
# the smallest that might fill in the gaps
# No need to create a 2D map, although, it is possible


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        coins = sorted([coin for coin in coins if coin <= amount])
        for coin in coins[::-1]:
            next_dp = [0] * (amount + 1)
            next_dp[0] = 1
            for a in range(amount + 1):
                next_dp[a] = dp[a]
                if a - coin >= 0:
                    next_dp[a] += next_dp[a - coin]
            dp = next_dp

        # print(dp)
        return dp[amount]
