class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0): return 0
        nums.sort()
        last_smaller=nums[0]
        last_count=1
        res=1
        for i in nums:
            if(last_smaller<i and last_smaller+1==i):
                last_smaller=i
                last_count+=1
            elif(last_smaller==i):
                continue
            else:
                last_smaller=i
                last_count=1
            res=max(res,last_count)
            print(last_smaller)
        return res


            