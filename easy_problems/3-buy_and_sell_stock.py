# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))