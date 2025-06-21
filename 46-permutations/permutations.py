from collections import defaultdict
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        h=defaultdict(bool)
        n=len(nums)
        def dfs(path):
            if(len(path[:])==n):
                res.append(path[:])
                return
            for i in nums:
                if(not h[i]):
                    h[i]=True
                    path.append(i)
                    dfs(path)
                    path.pop()
                    h[i]=False
        dfs([])
        return res