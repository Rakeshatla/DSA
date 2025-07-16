class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        n=len(prices)
        if(n==1):
            return 0
        for i in range(1,n):
            mini=min(mini,prices[i])
            profit+=prices[i]-mini
            mini=prices[i]
        return profit