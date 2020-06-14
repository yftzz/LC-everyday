class Solution:
    def maxProfit(self, prices):
        profit = 0
        ptr = -1
        bought = False
        prices.append(-1)
        for i in range(0, len(prices) - 1):
            if not bought:
                if prices[i + 1] > prices[i]:
                    bought = True
                    ptr = prices[i]
            else:
                if prices[i + 1] < prices[i]:
                    profit += prices[i] - ptr
                    bought = False
        return profit



# -------------------- My improved --------------------
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        income = 0
        buy_in = -1
        for i in range(len(prices)-1):
            if buy_in < 0:
                if prices[i + 1] > prices[i]:
                    buy_in = prices[i]
            else:
                if prices[i + 1] < prices[i]:
                    income = income + prices[i] - buy_in
                    buy_in = -1
                    
        if buy_in >= 0:
            income = income + prices[-1] - buy_in
                    
        return income




class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        income = 0
        for i in range(len(prices) - 1):
            income += max(0, prices[i + 1] - prices[i])
        return income