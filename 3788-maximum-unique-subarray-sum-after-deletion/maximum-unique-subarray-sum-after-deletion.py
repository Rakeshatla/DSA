from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        a=set()
        for i in nums:
            if i>0:
                a.add(i)
        if(len(a)==0):
            return max(nums)
        return sum(a)