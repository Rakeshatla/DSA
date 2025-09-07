from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        maxx=0
        m=len(grid)
        n=len(grid[0])
        visited=[[0 for _ in range(n)]for _ in range(m)]
        queue=deque()
        for i in range(m):
            for j in range(n):
                if(i==0 or i==m-1):
                    if(grid[i][j]==1):
                        queue.append([i,j])
                        visited[i][j]=1
                if(j==0 or j==n-1):
                    if(grid[i][j]==1):
                        queue.append([i,j])
                        visited[i][j]=1
        while queue:
            node=queue.popleft()
            r=node[0]
            c=node[1]
            drow=[-1,0,1,0]
            dcol=[0,1,0,-1]
            for i in range(4):
                nr=r+drow[i]
                nc=c+dcol[i]
                if(nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1 and visited[nr][nc]!=1):
                    queue.append([nr,nc])
                    visited[nr][nc]=1
        for i in range(m):
            for j in range(n):
                if(visited[i][j]==0 and grid[i][j]==1):
                    maxx+=1
        return maxx
                
        
