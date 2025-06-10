class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro=0
        curr=float('inf')
        for i in prices:
            if curr>i:
                curr=i
            profit=i-curr
            if(pro<profit):
                pro=profit
        return pro

