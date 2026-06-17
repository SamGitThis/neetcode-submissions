class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)
        best = 0

        while r < n:
            if prices[l] < prices[r]:
                best = max(best, (prices[r]- prices[l]))
            
            else:
                l = r

            r += 1

        return best