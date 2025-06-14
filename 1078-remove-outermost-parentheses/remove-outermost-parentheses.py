class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=''
        i=0
        start=0
        for j in range(len(s)):
            if(s[j]=='('):
                i+=1
                if(i==2):
                    start=j
            elif(s[j]==')'):
                i-=1
                if(i==1):
                    res+=s[start:j+1]
                    start=0
        return res
            
