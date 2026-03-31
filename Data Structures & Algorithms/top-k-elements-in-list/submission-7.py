class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        placeMent = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num, app in freq.items():
            placeMent[app].append(num)
        
        res = []
        for i in range(len(placeMent) -1, -1, -1):
            for num in placeMent[i]:
                res.append(num)
                if len(res) == k:
                    return res