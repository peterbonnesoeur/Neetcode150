#First sliding window exemple. Once we see adecrease in the prices, we log thetime when this happened.
# Then,we just do a maximum of the difference between price[r] and price[l] and compare it to the last max result.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res