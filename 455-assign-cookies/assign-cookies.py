class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m=len(g)
        n=len(s)
        i,j=0,0
        count=0
        while(i<m and j<n):
            if(s[j]>=g[i]):
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count
