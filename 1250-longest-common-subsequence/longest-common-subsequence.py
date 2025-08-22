class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        def dfs(i,j,memo):
            if(i<0 or j<0):
                return 0
            if((i,j) in memo):
                return memo[(i,j)]
            if(text1[i]==text2[j]):
                res=1+dfs(i-1,j-1,memo)
            else:
                res=max(dfs(i-1,j,memo),dfs(i,j-1,memo))
            memo[(i,j)]=res
            return res
        return dfs(n-1,m-1,{})