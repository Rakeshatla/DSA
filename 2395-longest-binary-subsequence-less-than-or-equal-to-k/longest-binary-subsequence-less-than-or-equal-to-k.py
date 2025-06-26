class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        t=0
        cnt=0
        res=0
        for i in range(len(s)):
            j=-i-1
            cnt+=int(s[j])*(2**t)
            t+=1
            if(cnt<=k):
                res+=1
            elif(cnt>k and s[j]=='0'):
                res+=1
        return res