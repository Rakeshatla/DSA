from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original=image[sr][sc]
        m=len(image)
        n=len(image[0])
        visited=image.copy()
        queue=deque([[sr,sc]])
        visited[sr][sc]=color
        while queue:
            node=queue.popleft()
            print(node)
            r=node[0]
            c=node[1]
            # print(r,c)
            drow=[-1,0,1,0]
            dcol=[0,1,0,-1]
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if(nrow>=0 and nrow<m and ncol>=0 and ncol<n and image[nrow][ncol]==original and visited[nrow][ncol]!=color):
                    visited[nrow][ncol]=color
                    queue.append([nrow,ncol])
        return visited

