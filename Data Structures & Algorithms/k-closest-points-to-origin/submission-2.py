class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for nums in points:
            dist = nums[0] **2 + nums[1]**2
            minHeap.append([dist, nums[0], nums[1]])
        heapq.heapify(minHeap)
        res = []
        while len(res) < k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res