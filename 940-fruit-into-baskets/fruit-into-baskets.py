from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxx=0
        curr=0
        l=0
        h=defaultdict(int)
        for r in range(len(fruits)):
            h[fruits[r]]+=1
            while(len(h)>2):
                h[fruits[l]]-=1
                if(h[fruits[l]]==0):
                    curr-=h[fruits[l]]
                    del h[fruits[l]]
                l+=1
            curr=sum(h.values())
            maxx=max(maxx,curr)
            # print(h)
        return maxx
                
            