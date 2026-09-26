class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        def backtrack(index, num):
            if index == len(nums):
                self.res += num
                return
            backtrack(index + 1, num ^ nums[index])
            backtrack(index + 1, num)
        backtrack(0, 0)
        return self.res