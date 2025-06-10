class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        p=0
        n=0
        for i in nums:
            if(i>0):
                res[2*p]=i
                p+=1
            else:
                res[2*n+1]=i
                n+=1
        return res

        