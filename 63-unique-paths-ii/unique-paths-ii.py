class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        def dfs(i,j,memo):
            if(i>=0 and j>=0 and obstacleGrid[i][j]==1):
                return 0
            if((i,j) in memo):
                return memo[(i,j)]
            if(i==0 and j==0):
                return 1
            if(i<0 or j<0):
                return 0
            up=dfs(i-1,j,memo)
            down=dfs(i,j-1,memo)
            memo[(i,j)]=up+down
            return memo[(i,j)]
        return dfs(m-1,n-1,{})