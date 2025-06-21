from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt=Counter(word)
        ans=float('inf')
        val=sorted(cnt.values())
        for i in val:
            dell=0
            for j in val:
                if(i>j):
                    dell+=j
                elif(j-i>k):
                    dell+=j-i-k
            ans=min(ans,dell)
        return ans