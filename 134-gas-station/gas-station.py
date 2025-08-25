class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)):
            return -1
        dif=[]
        n=len(gas)
        for i in range(n):
            dif.append(gas[i]-cost[i])
        total=0
        index=0
        flag=0
        for i in range(len(dif)):
            total+=dif[i]
            if(flag==0 and total>=0):
                index=i
                flag=1
            if(total<0):
                total=0
                index=0
                flag=0
        return index