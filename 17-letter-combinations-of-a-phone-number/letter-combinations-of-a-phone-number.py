class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits==''):
            return []
        res=[]
        h={'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def dfs(ind,currStr):
            if(len(currStr)==len(digits)):
                res.append(currStr)
                return
            for i in h[digits[ind]]:
                dfs(ind+1,currStr+i)
        dfs(0,'')
        return res