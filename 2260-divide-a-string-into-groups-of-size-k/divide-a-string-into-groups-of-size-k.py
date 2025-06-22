class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        i=0
        n=len(s)
        while(i+(k-1)<n):
            res.append(s[i:i+k])
            i+=(k-1)+1
        # print(i)
        if(i<=n-1):
            a=''
            a+=fill*(k-(n-i))
            res.append(s[i:]+a)
        return res