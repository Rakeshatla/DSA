class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            return nums[0]
        def robb(nums):
            n=len(nums)
            prev=nums[0]
            prev2=0
            for i in range(1,n):
                take=nums[i]
                if(i>1):
                    take+=prev2
                nottake=0+prev
                curr=max(take,nottake)
                prev2=prev
                prev=curr
            return prev
        temp1,temp2=[],[]
        for i in range(len(nums)):
            if(i!=0):
                temp1.append(nums[i])
            if(i!=n-1):
                temp2.append(nums[i])
        return max(robb(temp1),robb(temp2))