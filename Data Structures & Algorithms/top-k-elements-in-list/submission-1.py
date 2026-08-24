class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hist = defaultdict(int)
        # for i in nums:
        #     hist[i] += 1
        # sorted_hist = dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))
        # return list(sorted_hist.keys())[:k]
        return [x for x, _ in Counter(nums).most_common(k)]