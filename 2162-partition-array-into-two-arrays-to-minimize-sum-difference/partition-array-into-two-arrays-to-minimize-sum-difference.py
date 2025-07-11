class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2 
        def get_sums(nums): 
            ans = {}
            N = len(nums)
            for k in range(1, N+1): 
                sums = []
                for comb in combinations(nums, k):
                    s = sum(comb)
                    sums.append(s)
                ans[k] = sums
            return ans
        
        left_part, right_part = nums[:N], nums[N:]
        left_sums, right_sums = get_sums(left_part), get_sums(right_part)
        ans = abs(sum(left_part) - sum(right_part)) 
        total = sum(nums) 
        half = total // 2 
        for k in range(1, N):
            left = left_sums[k] 
            right = right_sums[N-k] 
            right.sort() 
            for x in left:
                r = half - x 
                p = bisect.bisect_left(right, r) 
                for q in [p, p-1]:
                    if 0 <= q < len(right):
                        left_ans_sum = x + right[q]
                        right_ans_sum = total - left_ans_sum
                        diff = abs(left_ans_sum - right_ans_sum)
                        ans = min(ans, diff) 
        return ans