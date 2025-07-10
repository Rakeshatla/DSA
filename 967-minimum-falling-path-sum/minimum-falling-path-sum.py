class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0 for _ in range(n)]for _ in range(m)]
        for j in range(len(matrix[0])):
            dp[0][j]=matrix[0][j]
        for i in range(1,m):
            for j in range(n):
                up=matrix[i][j]+dp[i-1][j]
                right=matrix[i][j]+(dp[i-1][j+1] if j<n-1 else float('inf'))
                left=matrix[i][j]+(dp[i-1][j-1]if j>0 else float('inf'))
                dp[i][j]=min(up,right,left)
        maxx=dp[n-1][0]
        for j in range(n):
            maxx=min(maxx,dp[n-1][j])
        return maxx