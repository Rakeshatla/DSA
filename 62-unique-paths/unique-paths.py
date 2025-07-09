class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i,j,memo):
            if(i==m-1 and j==n-1):
                return 1
            if(i>m-1 or j>n-1):
                return 0
            if((i,j) in memo):
                return memo[(i,j)]
            memo[(i,j)]=dfs(i+1,j,memo)+dfs(i,j+1,memo)
            return memo[(i,j)]
        return dfs(0,0,{})