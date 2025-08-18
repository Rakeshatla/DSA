class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i,memo):
            if i in memo:
                return memo[i]
            if(i==0):
                return 1
            if(i<0):
                return 0
            one=dfs(i-1,memo)
            two=dfs(i-2,memo)
            memo[i]=one+two
            return memo[i]
        return dfs(n,{})