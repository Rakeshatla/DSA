class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            take=nums[i]
            if(i>1):
                take+=dp[i-2]
            nottake=0+dp[i-1]
            dp[i]=max(take,nottake)
        return dp[n-1]
