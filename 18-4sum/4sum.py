class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sett=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                l=j+1
                h=n-1
                while(l<h):
                    summ=nums[i]+nums[j]+nums[l]+nums[h]
                    if(summ==target):
                        sett.add(tuple([nums[i],nums[j],nums[l],nums[h]]))
                        l+=1
                        h-=1
                    elif(summ<target):
                        l+=1
                    else:
                        h-=1
        return list(sett)
                    