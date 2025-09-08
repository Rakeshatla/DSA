from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if(grid[0][0]==1 or grid[m-1][n-1]==1):
            return -1
        drow=[-1,-1,-1,0,1,1,1,0]
        dcol=[-1,0,1,1,1,0,-1,-1]
        dis=[[float('inf') for _ in range(n)]for _ in range(m)]
        queue=deque([[0,[0,0]]])
        dis[0][0]=0
        while queue:
            node=queue.popleft()
            print(node)
            wt=node[0]
            r=node[1][0]
            c=node[1][1]
            if(r*c==(m-1)*(n-1)):
                return dis[r][c]+1
            for i in range(8):
                nr=r+drow[i]
                nc=c+dcol[i]
                if(nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==0):
                    if(wt+1<dis[nr][nc]):
                        dis[nr][nc]=wt+1
                        queue.append([wt+1,[nr,nc]])
        return -1

