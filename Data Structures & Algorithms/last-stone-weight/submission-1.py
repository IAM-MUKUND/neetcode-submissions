class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for i in stones:
            heapq.heappush(maxHeap, -i)
        
        while len(maxHeap) > 1:
            x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if x > y:
                heapq.heappush(maxHeap, -(x - y))
        return -maxHeap[0] if maxHeap else 0