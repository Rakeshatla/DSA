class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            n = len(nums)
            l = n - 2
            while l >= 0 and nums[l] >= nums[l + 1]:
                l -= 1
            if l >= 0:
                h = n - 1
                while nums[h] <= nums[l]:
                    h -= 1
                # Step 3: Swap them
                nums[l], nums[h] = nums[h], nums[l]
            
            # Step 4: Reverse the sublist after index l
            left = l + 1
            right = n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
