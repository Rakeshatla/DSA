class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res=[]
        m=len(mat)
        n=len(mat[0])
        row=0
        col=0
        up=1
        while(row<m and col<n):
            if(up==1):
                while(row>0 and col<n-1):
                    res.append(mat[row][col])
                    row-=1
                    col+=1
                res.append(mat[row][col])
                if(col==n-1):
                    row+=1
                else:
                    col+=1
            else:
                while(col>0 and row<m-1):
                    res.append(mat[row][col])
                    row+=1
                    col-=1
                res.append(mat[row][col])
                if(row==m-1):
                    col+=1
                else:
                    row+=1
            if(up==1):
                up=0
            else:
                up=1
        return res
