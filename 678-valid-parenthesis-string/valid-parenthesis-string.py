class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        minn=0
        maxx=0
        for i in s:
            if(i=='('):
                minn+=1
                maxx+=1
            if(i==')'):
                minn-=1
                maxx-=1
            if(i=='*'):
                minn-=1
                maxx+=1
            if(minn<0):
                minn=0
            if(maxx<0):
                return False
        return minn==0
