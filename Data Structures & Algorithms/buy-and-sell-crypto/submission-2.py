# O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            max_profit = max(prices[right]-prices[left], max_profit)
            right += 1
        return max_profit