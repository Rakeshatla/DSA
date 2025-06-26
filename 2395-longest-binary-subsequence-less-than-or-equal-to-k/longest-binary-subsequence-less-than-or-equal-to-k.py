class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        s=s[::-1]
        t=0
        cnt=0
        res=0
        for i in s:
            cnt+=int(i)*(2**t)
            t+=1
            if(cnt<=k):
                res+=1
            elif(cnt>k and i=='0'):
                res+=1
        return res