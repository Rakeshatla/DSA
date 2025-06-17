class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        cnt=0
        ans=bin(ans)
        ans=ans[2:]
        ans=str(ans)
        for i in ans:
            if(i=='1'):
                cnt+=1
        return cnt