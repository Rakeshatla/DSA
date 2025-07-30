class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx=max(nums)
        size=0
        maxi=0
        for i in range(len(nums)):
            if(nums[i]==maxx):
                size+=1
                maxi=max(size,maxi)
            else:
                size=0
        return maxi

