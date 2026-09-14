class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pref, suff = 1, 1
        for index in range(n):
            res[index] = pref
            pref *= nums[index]
        for index in range(n - 1, -1, -1):
            res[index] *= suff
            suff *= nums[index]
        return res
