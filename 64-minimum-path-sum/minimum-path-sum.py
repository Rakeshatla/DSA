class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j,memo):
            if((i,j) in memo):
                return memo[(i,j)]
            if(i==0 and j==0):
                return grid[0][0]
            if(i<0 or j<0):
                return float('inf')
            up=grid[i][j]+dfs(i-1,j,memo)
            left=grid[i][j]+dfs(i,j-1,memo)
            memo[(i,j)]=min(up,left)
            return memo[i,j]
        return dfs(m-1,n-1,{})