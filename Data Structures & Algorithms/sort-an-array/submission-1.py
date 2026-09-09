class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        heapq.heapify(nums)
        n = len(nums)
        for _ in range(n):
            res.append(heapq.heappop(nums))
        return res