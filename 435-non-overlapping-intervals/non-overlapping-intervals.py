class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        # print(intervals)
        n=len(intervals)
        cnt=1
        last=intervals[0][1]
        for i in range(1,n):
            # print(intervals[i])
            for j in range(len(intervals[i])):
                if(intervals[i][0]>=last):
                    cnt+=1
                    last=intervals[i][1]
        return n-cnt

