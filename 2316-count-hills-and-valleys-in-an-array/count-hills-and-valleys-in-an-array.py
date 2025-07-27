class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev=nums[0]
        count=0
        n=len(nums)
        for i in range(1,n-1):
            if(prev==nums[i]):
                continue
            nextt=nums[i+1]
            if(nums[i]==nextt):
                continue
            # print(prev,nextt,'i',i)
            if(nums[i]>prev and nums[i]>nextt):
                count+=1
            elif(nums[i]<prev and nums[i]<nextt):
                count+=1
            prev=nums[i]
        return count
            

