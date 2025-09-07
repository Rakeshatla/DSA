class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        visited=[[0 for _ in range(n)]for _ in range(m)]
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        def dfs(r,c,visited,board,drow,dcol):
            visited[r][c]=1
            for i in range(4):
                nr=r+drow[i]
                nc=c+dcol[i]
                if(nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]!=1 and board[nr][nc]=='O'):
                    dfs(nr,nc,visited,board,drow,dcol)
        for j in range(n):
            if(visited[0][j]!=1 and board[0][j]=='O'):
                dfs(0,j,visited,board,drow,dcol)
            if(visited[m-1][j]!=1 and board[m-1][j]=='O'):
                dfs(m-1,j,visited,board,drow,dcol)
        for i in range(m):
            if(visited[i][0]!=1 and board[i][0]=='O'):
                dfs(i,0,visited,board,drow,dcol)
            if(visited[i][n-1]!=1 and board[i][n-1]=='O'):
                dfs(i,n-1,visited,board,drow,dcol)
        for i in range(m):
            for j in range(n):
                if(visited[i][j]==0 and board[i][j]=='O'):
                    board[i][j]='X'
        return board
        