import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        pq=[(-v,k) for k,v in counter.items()]
        heapq.heapify(pq)
        res=''
        # print(counter)
        while pq:
            v,k=heapq.heappop(pq)
            res+=k*-v
        return res

