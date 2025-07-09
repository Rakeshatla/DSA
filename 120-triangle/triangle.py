class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        def dfs(i,j,memo):
            if((i,j) in memo):
                return memo[(i,j)]
            if(i==n-1):
                return triangle[n-1][j]
            d=triangle[i][j]+dfs(i+1,j,memo)
            dg=triangle[i][j]+dfs(i+1,j+1,memo)
            memo[(i,j)]=min(d,dg)
            return memo[(i,j)]
        return dfs(0,0,{})
