class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        i=0
        while(i<n-2):
            if(nums[i+2]-nums[i]<=k):
                res.append(nums[i:i+3])
            else:
                return []
            i+=3
        # print(len(res))
        return res