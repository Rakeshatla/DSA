class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        def dfs(i,target,memo):
            if(i==0):
                if(target%coins[0]==0):
                    return target//coins[0]
                else:
                    return float('inf')
            if((i,target) in memo):
                return memo[(i,target)]
            nopick=dfs(i-1,target,memo)
            pick=float('inf')
            if(coins[i]<=target):
                pick=1+dfs(i,target-coins[i],memo)
            memo[(i,target)]=min(pick,nopick)
            return min(pick,nopick)
        a=dfs(n-1,amount,{})
        return -1 if a==float('inf') else a
