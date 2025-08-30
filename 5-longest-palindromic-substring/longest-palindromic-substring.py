class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if(s==s[::-1]):
            return s
        # if(n<=2):
        #     return s[0]
        res=s[0]
        for i in range(n):
            for j in range(i+1,n):
                ss=s[i:j+1]
                if(ss==ss[::-1] and len(ss)>len(res)):
                    res=ss
                else:
                    continue
        return res
        