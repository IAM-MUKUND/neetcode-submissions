class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = dict()
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hist:
                return [hist[a], i]
            else:
                hist[nums[i]] = i