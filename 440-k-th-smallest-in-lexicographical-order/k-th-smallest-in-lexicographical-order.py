class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def precount(prefix,n):
            count1=0
            curr=prefix
            next1=prefix+1
            while(curr<=n):
                count1+=min(n+1,next1)-curr
                curr*=10
                next1*=10
            return count1
        prefix=1
        k-=1
        while(k>0):
            cnt=precount(prefix,n)
            print(cnt)
            if(cnt<=k):
                prefix+=1
                k-=cnt
            else:
                prefix*=10
                k-=1
        return prefix