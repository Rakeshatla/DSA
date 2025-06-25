class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if(n==1):
            return 0
        lmax=0
        rmax=0
        l=0
        total=0
        r=n-1
        while(l<r):
            if(height[l]<=height[r]):
                if(lmax>height[l]):
                    total+=lmax-height[l]
                else:
                    lmax=max(lmax,height[l])
                l+=1
            else:
                if(rmax>height[r]):
                    total+=rmax-height[r]
                else:
                    rmax=max(rmax,height[r])
                r-=1
            
        return total
