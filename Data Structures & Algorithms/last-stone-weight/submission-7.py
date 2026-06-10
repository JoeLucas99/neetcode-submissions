class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for n in stones:
            maxHeap.append(-n)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x , y = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if x < y:
                diff = x-y
                heapq.heappush(maxHeap, diff)
        return abs(maxHeap[0]) if maxHeap else 0
        