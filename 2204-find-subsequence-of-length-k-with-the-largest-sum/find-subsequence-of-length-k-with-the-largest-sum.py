class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        s=[]
        for i in range(len(nums)):
            s.append([i,nums[i]])
        s.sort(key=lambda x:x[1],reverse=True)
        s=s[:k]
        s.sort(key=lambda x:x[0])
        res=[]
        for i in range(k):
            res.append(s[i][1])
        return res