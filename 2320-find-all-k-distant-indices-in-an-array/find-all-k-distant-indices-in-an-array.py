class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        li=[]
        for i in range(len(nums)):
            if(nums[i]==key):
                li.append(i)
        res=[]
        for i in range(len(nums)):
            nearest=min(li,key=lambda x:abs(x-i))
            if(abs(i-nearest)<=k):
                res.append(i)
            else:
                continue
        return res        