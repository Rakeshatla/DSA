class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        res=[]
        n=len(startTime)
        if(startTime[0]>0):
            res.append(startTime[0])
        for i in range(n-1):
            res.append(abs(endTime[i]-startTime[i+1]))
        if(endTime[-1]<eventTime):
            res.append(abs(eventTime-endTime[-1]))
        print(res)
        l=0
        maxx=sum(res[:k+1])
        summ=maxx
        for r in range(k+1,len(res)):
            maxx=max(maxx,summ)
            summ+=res[r]
            summ-=res[l]
            l+=1
        maxx=max(maxx,summ)
        return maxx


        