class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(row,col,ans,img,delrow,delcol,color,inicolor):
            ans[row][col]=color
            n=len(image)
            m=len(image[0])
            for i in range(4):
                roww=row+delrow[i]
                coll=col+delcol[i]
                if(roww>=0 and roww<n and coll>=0 and coll<m and image[roww][coll]==inicolor and ans[roww][coll]!=color):
                    dfs(roww,coll,ans,img,delrow,delcol,color,inicolor)
        ans=image
        inicolor=image[sr][sc]
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        dfs(sr,sc,ans,image,delrow,delcol,color,inicolor)
        return ans
        