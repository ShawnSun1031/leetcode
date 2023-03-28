class Solution:
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        min = prices[0]
        output = 0
        for p in prices:
            temp = p - min
            if temp > output:
                output = temp
            if p < min:
                min = p
        return output
""" two pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        
        while r < len(prices):
            if prices[l] <= prices[r]:
                profit = max(profit,prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return profit
"""


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    ans = Solution().maxProfit(prices)
    print(ans)