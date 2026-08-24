class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pref, suff = 1, 1
        for i in range(n):
            res[i] = pref
            pref *= nums[i]
        for j in range(n - 1, -1, -1):
            res[j] *= suff
            suff *= nums[j]
        return res
        
