class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        bought = False
        buy_in = -1
        max_prof = -1
        prices.append[-1]
        for i in range(len(prices)-1):
            if bought and prices[i + 1] < prices[i]:
                if prices[i] - buy_in > max_prof:
                    max_prof = prices[i] - buy_in
                bought = False
            if not bought and prices[i + 1] > prices[i]:
                buy_in = prices[i]
                bought = True
        if bought and prices[len(prices)-1]-buy_in > max_prof:
            max_prof = prices[len(prices)-1]-buy_in > max_prof
        return max_prof



# ---------------improved---------------
    def maxProfit(self, prices):
        max_prof = -1
        min_val = float('int')
        max_val = -1

        for price in prices:
            min_val = min(price, min_val)
            max_prof = max(max_prof, price-min_val)
        return max_prof