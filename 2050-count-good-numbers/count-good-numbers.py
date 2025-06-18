class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        def mod1(a,b):
            res=1
            while(b>0):
                if(b&1):
                    res=(res*a)%mod
                    b-=1
                a=a*a%mod
                b>>=1
            return res
        odd=n>>1
        even=(n+1)//2
        return mod1(5,even)*mod1(4,odd)%mod