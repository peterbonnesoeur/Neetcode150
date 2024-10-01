# To redo, this is a dfs problem 100%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):

            if i>= len(prices):
                return 0
            elif (i, buying) in dp:
                return dp[(i, buying)]
        
            nothing = dfs(i+1, buying)

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, nothing)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, nothing)
            return dp[(i, buying)]

        return dfs(0, True)