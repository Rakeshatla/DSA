class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        l=0
        n=len(s)
        res=0
        for r in range(len(s)):
            while(s[r] in sett):
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            res=max(res,r-l+1)
        return res
