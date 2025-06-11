class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        summp=1
        summs=1
        for i in range(len(nums)):
            if(summp==0):
                summp=1
            if(summs==0):
                summs=1
            j=-i-1
            summp*=nums[i]
            summs*=nums[j]
            res=max(res,max(summp,summs))
        return res