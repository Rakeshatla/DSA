class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        max_length = 1
        
        # Check all 4 possible patterns: (first_parity, second_parity)
        for first in [0, 1]:  # 0 = even, 1 = odd
            for second in [0, 1]:
                length = 0
                expecting = first  # What parity we're looking for next
                
                for num in nums:
                    if num % 2 == expecting:
                        length += 1
                        # Alternate between first and second parity
                        expecting = first if expecting == second else second
                
                max_length = max(max_length, length)
        
        return max_length