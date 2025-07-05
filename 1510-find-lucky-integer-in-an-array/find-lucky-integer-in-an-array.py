from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h=defaultdict(int)
        for i in arr:
            h[i]+=1
        res=float('-inf')
        for k,v in h.items():
            if(k==v):
                res=max(res,k)
        return res if res!=float('-inf') else -1
            