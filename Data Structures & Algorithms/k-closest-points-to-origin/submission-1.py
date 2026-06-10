class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        heapq.heapify(minHeap)
        for pair in points:
            x, y = pair[0], pair [1]
            sqrDist = x**2 + y**2
            heapq.heappush(minHeap, [sqrDist, x, y])
        for i in range(k):
            sqrDist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res