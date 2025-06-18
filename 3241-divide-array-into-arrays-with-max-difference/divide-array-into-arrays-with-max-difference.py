class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        i=0
        print(nums)
        while(i<n-2):
            if(abs(nums[i]-nums[i+2])<=k):
                res.append(nums[i:i+3])
            i+=3
        # print(len(res))
        return res if len(res)==(n//3) else []