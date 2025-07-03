class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        h={}
        maxx=0
        l=0
        for r in range(n):
            if s[r] in h:
                h[s[r]]+=1
            else:
                h[s[r]]=1
            v=max(h.values())
            if((r-l+1)-v>k):
                h[s[l]]-=1
                l+=1
                v=0
            maxx=max(maxx,r-l+1)
        return maxx
            



    