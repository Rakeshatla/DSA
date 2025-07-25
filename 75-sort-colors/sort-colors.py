class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        mid=0
        low=0
        high=n-1
        for i in range(n):
            if(nums[mid]==0):
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif(nums[mid]==1):
                mid+=1
            elif(nums[mid]==2):
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
        return nums
        