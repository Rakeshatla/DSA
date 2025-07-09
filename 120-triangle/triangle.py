class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1 for i in range(j+1)] for j in range(n)]
        def dfs(i,j,memo):
            if(memo[i][j]!=-1):
                return memo[i][j]
            if(i==n-1):
                return triangle[n-1][j]
            d=triangle[i][j]+dfs(i+1,j,memo)
            dg=triangle[i][j]+dfs(i+1,j+1,memo)
            memo[i][j]=min(d,dg)
            return memo[i][j]
        return dfs(0,0,dp)
