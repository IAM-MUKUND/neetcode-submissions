class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref, suff = [1], [1]
        n = len(nums)
        for i in range(1, n):
            prod = pref[-1] * nums[i - 1]
            pref.append(prod)
        for j in range(n - 1, 0, -1):
            prod = suff[-1] * nums[j]
            suff.append(prod)
        suff = suff[::-1]

        for i in range(n):
            res.append(pref[i] * suff[i])
        return res
        
