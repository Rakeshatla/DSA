class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            one=dp[i-1]
            two=0
            if(n>1):
                two=dp[i-2]
            dp[i]=one+two
        print(dp)
        return dp[n]
