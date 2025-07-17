class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd=0
        even=0
        alter=1
        flag=nums[0]%2
        for i in nums:
            if(i&1==1):
                odd+=1
            if(i&1!=1):
                even+=1
            curr=i%2
            if(i>0 and flag!=curr):
                alter+=1
                flag=curr
        return max(odd,even,alter)
