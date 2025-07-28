class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxx=0
        n=len(nums)
        for i in nums:
            maxx|=i
        def dfs(orr,ind):
            # if(orr==maxx):
            #     return 1
            if(ind>=n):
                return 1 if orr==maxx else 0
            notake=dfs(orr,ind+1)
            take=dfs(orr|nums[ind],ind+1)
            # print(orr)
            return take+notake
        return dfs(0,0)