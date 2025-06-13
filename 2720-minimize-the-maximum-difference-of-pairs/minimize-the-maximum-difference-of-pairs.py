class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if(p==0):
            return 0
        def check(nums,diff):
            count=0
            i=0
            n=len(nums)
            while(i<n-1):
                if(nums[i+1]-nums[i]<=diff):
                    count+=1
                    i+=1
                i+=1
            return count
        nums.sort()
        # print(nums)
        n=len(nums)
        res=0
        l=0
        h=nums[n-1]-nums[0]
        while(l<=h):
            mid=(l+h)//2
            # print('m',mid)
            co=check(nums,mid)
            # print(co)
            if(co>=p):
                res=mid
                h=mid-1
            else:
                l=mid+1
        return res
        