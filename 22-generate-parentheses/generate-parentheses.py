class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        ans=[]
        def dfs(openn,close):
            if(len(ans)==2*n):
                res.append(''.join(ans))
                return
            if(openn<n):
                ans.append('(')
                dfs(openn+1,close)
                ans.pop()
            if(openn>close):
                ans.append(')')
                dfs(openn,close+1)
                ans.pop()
        dfs(0,0)
        return res
