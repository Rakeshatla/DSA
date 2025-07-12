class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0 for _ in range(amount+1)]for _ in range(n)]
        for i in range(n):
            dp[i][0]=1
        for j in range(amount+1):
            if(j%coins[0]==0):
                dp[0][j]=1
            else:
                dp[i][coins[0]]=0
        for i in range(1,n):
            for j in range(amount+1):
                notake=dp[i-1][j]
                take=0
                if(coins[i]<=j):
                    take=dp[i][j-coins[i]]
                dp[i][j]=take+notake
        # print(dp)
        return dp[n-1][amount]
