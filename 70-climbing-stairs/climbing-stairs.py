class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(ind,memo={}):
            if(ind<=1):
                return 1
            if ind in memo:
                return memo[ind]
            memo[ind]=dfs(ind-1,memo)+dfs(ind-2,memo)
            return memo[ind]
        return dfs(n,{})
        