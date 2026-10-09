class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        lowest = [prices[buy]]
        for x in range(1, len(prices)):
            if prices[x] < prices[buy]:
                lowest.append(prices[x])
                buy = x
            else:
                lowest.append(prices[buy])

        maxProfit = 0
        for x in range(1, len(prices)):
            if prices[x] - lowest[x] > maxProfit:
                maxProfit = prices[x] - lowest[x]
            
        return maxProfit
        