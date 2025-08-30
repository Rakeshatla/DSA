class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        res=''
        for i in range(len(s)):
            if(count==0):
                start=i
            if(s[i]=='('):
                count+=1
            elif(s[i]==')'):
                count-=1
            if count==0:
                res+=s[start+1:i]
        return res

