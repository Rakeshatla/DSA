class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary_search(res, n):
            left = 0
            right = len(res) - 1
            ans=0
            while left <= right:
                mid = (left + right) // 2
                if res[mid] >= n:
                    ans=mid
                    right=mid-1
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return ans

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n
        
        return len(res)