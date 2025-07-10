class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if(summ&1==1):
            return False
        target=summ//2
        n=len(nums)
        dp=[[False for _ in range(target+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1,n):
            for j in range(1,target+1):
                notake=dp[i-1][j]
                take=False
                if(nums[i]<=j):
                    take=dp[i-1][j-nums[i]]
                dp[i][j]=notake or take
        # print(dp)
        return dp[n-1][target]