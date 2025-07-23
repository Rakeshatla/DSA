class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=float('inf')
        n=len(nums)
        for i in range(n-2):
            l=i+1
            h=n-1
            while(l<h):
                summ=nums[i]+nums[l]+nums[h]
                if(abs(target-res)>abs(target-summ)):
                    res=summ
                elif(summ<target):
                    l+=1
                else:
                    h-=1
                # print(summ)
        return res

