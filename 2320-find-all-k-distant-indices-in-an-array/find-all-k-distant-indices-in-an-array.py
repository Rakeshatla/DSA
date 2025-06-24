class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = set()
        
        for i in range(n):
            if nums[i] == key:
                # mark all indices from max(0, i-k) to min(n-1, i+k)
                for j in range(max(0, i - k), min(n, i + k + 1)):
                    res.add(j)
                    
        return sorted(res)
