class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-gift for gift in gifts]
        heapq.heapify(maxHeap)

        for i in range(k):
            curr = - heapq.heappop(maxHeap)
            curr = int(curr ** 0.5)
            heapq.heappush(maxHeap, - curr)
        
        return - sum(maxHeap)