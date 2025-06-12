class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while(l<=h):
            mid=(l+h)//2
            if(nums[mid]==target):
                return mid
            elif(nums[l]<=nums[mid]):
                if(nums[l]<=target<=nums[mid]):
                    h=mid
                else:
                    l=mid+1
            else:
                if(nums[mid]<nums[h] and nums[mid]<=target<=nums[h]):
                    l=mid
                else:
                    h=mid-1
        return -1
        