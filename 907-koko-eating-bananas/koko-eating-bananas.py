import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        if(n==h):
            return max(piles)
        if(n==1 and piles[0]>h):
            return math.ceil(piles[0]/h)
        def koko(piles,k):
            tim=0
            for i in piles:
                tim+=math.ceil(i/k)
            return tim
        l=1
        h1=max(piles)
        while(l<=h1):
            mid=(l+h1)//2
            time_req=koko(piles,mid)        
            if(time_req<=h):
                ans=mid
                h1=mid-1
            else:
                l=mid+1
        return ans

        