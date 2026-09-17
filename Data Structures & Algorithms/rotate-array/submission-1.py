class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        k %= len(nums)
        n = len(nums)
        nums[:] = nums[n - k:] + nums[:n - k]