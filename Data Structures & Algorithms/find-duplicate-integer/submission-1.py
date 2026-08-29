class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = [False] * len(nums)

        for i in nums:
            if res[i]:
                return i
            res[i] = True