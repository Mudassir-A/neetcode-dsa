class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def bruteforce(prices):
            res = 0
            for i in range(len(prices)):
                buy = prices[i]
                for j in range(i + 1, len(prices)):
                    sell = prices[j]
                    res = max(res, sell - buy)
            return res

        def twoPointers(prices):
            l, r = 0, 1
            maxP = 0

            while r < len(prices):
                if prices[l] < prices[r]:
                    profit = prices[r] - prices[l]
                    maxP = max(maxP, profit)
                else:
                    l = r
                r+=1
            return maxP

        # return bruteforce(prices)
        return twoPointers(prices)
