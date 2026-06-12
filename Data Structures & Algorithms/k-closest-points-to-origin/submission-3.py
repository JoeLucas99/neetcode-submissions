class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for nums in points: #Time: n
            dist = nums[0] **2 + nums[1]**2
            minHeap.append([dist, nums[0], nums[1]])
        heapq.heapify(minHeap) #Time: logn
        res = []
        while len(res) < k: #Time: k
            dist, x, y = heapq.heappop(minHeap) #Time: logn
            res.append([x,y])
        return res