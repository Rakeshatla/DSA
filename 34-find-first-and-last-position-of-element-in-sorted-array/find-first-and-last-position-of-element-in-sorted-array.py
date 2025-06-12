class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a1=self.lower(nums,target)
        b1=self.upper(nums,target)
        return [a1,b1]
    def lower(self,a,x):
        l, h = 0, len(a) - 1
        res = -1
        while l <= h:
            mid = (l + h) // 2
            if a[mid] == x:
                res = mid
                h = mid - 1 
            elif(a[mid]<x):
                l = mid + 1 
            else:
                h=mid-1
        return res

    def upper(self,a,x):
        l, h = 0, len(a) - 1
        ans=-1
        while l <= h:
            mid = (l + h) // 2
            if a[mid] == x:
                ans=mid
                l=mid+1 
            elif(a[mid]<x):
                l = mid + 1  
            else:
                h=mid-1
        return ans
    