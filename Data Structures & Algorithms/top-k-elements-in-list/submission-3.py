class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hist = dict()
        # for num in nums:
        #     hist[num] = hist.get(num, 0) + 1
        # sorted_dict = dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))
        # return (list(sorted_dict.keys())[:k])
        return [x for x, _ in Counter(nums).most_common(k)]