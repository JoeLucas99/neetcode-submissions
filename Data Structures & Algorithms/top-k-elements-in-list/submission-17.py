class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numCnt = {}

        for num in nums:
            numCnt[num] = numCnt.get(num, 0) + 1
        buckets = [[] for i in range(len(nums) + 1)]
        
        for num, amnt in numCnt.items():
            buckets[amnt].append(num)
        
        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(num)
        return res