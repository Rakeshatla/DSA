class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moones voting algo
        ele=0
        count=0
        for i in nums:
            if(count==0):
                ele=i
            if(i==ele):
                count+=1
            else:
                count-=1
        return ele
        