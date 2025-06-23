class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cnt=0
        n=len(nums)
        if(n<=1):
            return True
        if(nums[0]==0):
            return False
        for i in range(len(nums)-1):
            if(i>cnt):
                return False
            cnt=max(cnt,i+nums[i])
        return cnt>=n-1