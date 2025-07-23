class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        co = self.reversePairs(left) + self.reversePairs(right)  # recursively count in each half
        i = j = 0
        # Count reverse pairs: left[i] > 2 * right[j]
        while i < len(left) and j < len(right):
            if left[i] > 2 * right[j]:
                co += len(left) - i  # all left[i:] will satisfy as left is sorted
                j += 1
            else:
                i += 1
        # Merge left and right into nums (so future merge steps are correct)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return co
