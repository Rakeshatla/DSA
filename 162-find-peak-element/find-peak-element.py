class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            return 0
        if(nums[0]>nums[1]):
            return 0
        if(nums[n-1]>nums[n-2]):
            return n-1
        l=0
        h=len(nums)
        while(l<=h):
            mid=(l+h)>>1
            if(nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]):
                return mid
            elif(nums[mid-1]>nums[mid]):
                h=mid-1
            else:
                l=mid+1
        