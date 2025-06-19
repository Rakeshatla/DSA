class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def dfs(ind,li):
            if ind>=n:
                res.append(li[:])
                return
            li.append(nums[ind])
            dfs(ind+1,li)
            li.pop()
            dfs(ind+1,li)
        dfs(0,[])
        return res
