class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = collections.deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time: 
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
        