

class Solution:

    def max_profit(self, prices):

        self.prices = prices
        self.profit = []
        self.helper(0, 0, 0)
        return max(self.profit)

    def helper(self, i, have, profit):
        if i == len(self.prices):
            return self.profit.append(profit)
        elif have:
            self.helper(i+1, 0, profit + self.prices[i])
            self.helper(i+1, 1, profit)
        else:
            self.helper(i+1, 0, profit)
            self.helper(i+1, 1, profit - self.prices[i])


    def max_profit2(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit


    def max_profit3(self, prices):
        pass