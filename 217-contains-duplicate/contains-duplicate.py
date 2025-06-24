class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)<=1):
            return False
        li=set()
        for i in nums:
            if(i in li):
                return True
            li.add(i)
        return False