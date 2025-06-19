class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt=0
        l=0
        n=len(nums)
        for r in range(n):
            if(nums[r]-nums[l]>k):
                cnt+=1
                l=r
        if(l==n-1):
            cnt+=1
        else:
            if(nums[r]-nums[l]<=k):
                cnt+=1
        return cnt