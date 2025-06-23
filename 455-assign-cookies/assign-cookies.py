class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l=0
        r=0
        cnt=0
        n=len(s)
        m=len(g)
        while(l<n and r<m):
            if(s[l]>=g[r]):
                cnt+=1
                l+=1
                r+=1
            else:
                l+=1
        return cnt

            
