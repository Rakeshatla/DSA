class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n,memo):
            if(n<0):
                return 0
            if(n==0):
                return 1
            if n in memo:
                return memo[n]
            one=dfs(n-1,memo)
            two=dfs(n-2,memo)
            memo[n]=one+two
            return memo[n]
        return dfs(n,{})
