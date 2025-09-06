from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        maxx=0
        visited=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):
                    queue.append([[i,j],0])
                    visited[i][j]=2
        while(queue):
            node=queue.popleft()
            r=node[0][0]
            c=node[0][1]
            t=node[1]
            maxx=max(maxx,t)
            drow=[-1,0,1,0]
            dcol=[0,1,0,-1]
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if(nrow>=0 and nrow<m and ncol>=0 and ncol<n and visited[nrow][ncol]==0 and grid[nrow][ncol]==1):
                    queue.append([[nrow,ncol],t+1])
                    visited[nrow][ncol]=2
        for i in range(m):
            for j in range(n):
                if(visited[i][j]!=2 and grid[i][j]==1):
                    return -1
        return maxx
