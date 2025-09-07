from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        visited=[[0  for _ in range(n)]for _ in range(m)]
        distance=[[0 for _ in range(n)]for _ in range(m)]
        queue=deque()
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):
                    queue.append([[i,j],0])
                    visited[i][j]=1
        while queue:
            node=queue.popleft()
            r=node[0][0]
            c=node[0][1]
            s=node[1]
            drow=[-1,0,1,0]
            dcol=[0,1,0,-1]
            distance[r][c]=s
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if(nrow>=0 and nrow<m and ncol>=0 and ncol<n and visited[nrow][ncol]!=1):
                    queue.append([[nrow,ncol],s+1])
                    visited[nrow][ncol]=1
        return distance
