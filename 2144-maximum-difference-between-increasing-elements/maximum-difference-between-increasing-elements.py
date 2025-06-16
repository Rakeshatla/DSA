class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        res=-1
        maxx=nums[n-1]
        for i in range(n-2,-1,-1):
            if(maxx>nums[i]):
                res=max(res,maxx-nums[i])
            else:
                maxx=nums[i]
        return res


