class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        k=min(k,n//2)
        # dp[ind][buy][trans]
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]
        for i in range(n+1):
            for j in range(2):
                dp[i][j][0]=0
        for i in range(2):
            for j in range(k+1):
                dp[n][i][j]=0
        for i in range(n-1,-1,-1):
            for j in range(2):
                for k1 in range(1,k+1):
                    if(j==1):
                        dp[i][1][k1]=max(-prices[i]+dp[i+1][0][k1],dp[i+1][1][k1])
                    else:
                        dp[i][0][k1]=max(prices[i]+dp[i+1][1][k1-1],dp[i+1][0][k1])
        return dp[0][1][k]